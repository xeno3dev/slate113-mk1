"""Run with KiCad's bundled Python. Uses only disposable in-memory boards."""
import unittest
import pcbnew
import wx
from unittest.mock import patch
with patch.object(pcbnew.ActionPlugin, "register"):
    from quick_unroute.plugin import (between_routing, component_nets, find_targets,
                                      UnrouteDialog, apply_targets)
from quick_unroute.paths import path_vertices


def position(x, y):
    return pcbnew.VECTOR2I(pcbnew.FromMM(x), pcbnew.FromMM(y))


def layer_set(layer):
    layers = pcbnew.LSET()
    layers.AddLayer(layer)
    return layers


class RoutingTests(unittest.TestCase):
    def setUp(self):
        self.board = pcbnew.BOARD()
        self.net = pcbnew.NETINFO_ITEM(self.board, "TEST")
        self.other_net = pcbnew.NETINFO_ITEM(self.board, "OTHER")
        self.board.Add(self.net)
        self.board.Add(self.other_net)
        self.a = self.footprint("J1", 0, 0)
        self.b = self.footprint("J2", 10, 0)
        self.main = [self.track(0, 0, 5, 0), self.track(5, 0, 10, 0)]
        self.branch = self.track(5, 0, 5, 5)
        self.island = self.track(20, 20, 25, 20)
        self.unrelated = self.track(0, 10, 10, 10, self.other_net)

    def footprint(self, ref, x, y):
        fp = pcbnew.FOOTPRINT(self.board)
        fp.SetReference(ref)
        pad = pcbnew.PAD(fp)
        pad.SetSize(position(1, 1))
        pad.SetPosition(position(x, y))
        pad.SetLayerSet(layer_set(pcbnew.F_Cu))
        pad.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
        pad.SetNet(self.net)
        fp.Add(pad)
        self.board.Add(fp)
        return fp

    def track(self, x1, y1, x2, y2, net=None, layer=pcbnew.F_Cu):
        track = pcbnew.PCB_TRACK(self.board)
        track.SetStart(position(x1, y1))
        track.SetEnd(position(x2, y2))
        track.SetWidth(pcbnew.FromMM(0.2))
        track.SetLayer(layer)
        track.SetNet(net or self.net)
        self.board.Add(track)
        return track

    def keys(self, items):
        return {item.m_Uuid.AsString() for item in items}

    def test_net_and_locked(self):
        self.branch.SetLocked(True)
        result = find_targets(self.board, component_nets([self.a]))
        self.assertEqual(self.keys(result), self.keys(self.main + [self.island]))
        self.assertEqual(len(find_targets(self.board, {self.net.GetNetCode()},
                                          include_locked=True)), 4)

    def test_component_connected_excludes_island(self):
        result = find_targets(self.board, footprints=[self.a], connected=True)
        self.assertEqual(self.keys(result), self.keys(self.main + [self.branch]))

    def test_between_excludes_branch_and_island(self):
        result = between_routing(self.board, [self.a, self.b])
        self.assertEqual(self.keys(result), self.keys(self.main))

    def test_alternate_path_and_dangling_loop(self):
        alternate = [self.track(0, 0, 0, -5), self.track(0, -5, 10, -5),
                     self.track(10, -5, 10, 0)]
        self.track(5, 5, 8, 5)
        self.track(8, 5, 8, 8)
        self.track(8, 8, 5, 5)
        result = between_routing(self.board, [self.a, self.b])
        self.assertEqual(self.keys(result), self.keys(self.main + alternate))

    def test_via_and_layer(self):
        self.main[1].SetLayer(pcbnew.B_Cu)
        via = pcbnew.PCB_VIA(self.board)
        via.SetPosition(position(5, 0))
        via.SetWidth(pcbnew.FromMM(0.6))
        via.SetDrill(pcbnew.FromMM(0.3))
        via.SetViaType(pcbnew.VIATYPE_THROUGH)
        via.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
        via.SetNet(self.net)
        self.board.Add(via)
        list(self.b.Pads())[0].SetLayerSet(layer_set(pcbnew.B_Cu))
        result = between_routing(self.board, [self.a, self.b])
        self.assertEqual(self.keys(result), self.keys(self.main + [via]))

    def test_no_connection_and_net_filter(self):
        self.assertEqual(between_routing(self.board, [self.a]), [])
        self.assertEqual(between_routing(self.board, [self.a, self.b], set()), [])
        self.board.RemoveNative(self.main[1])
        self.assertEqual(between_routing(self.board, [self.a, self.b]), [])

    def test_select_then_delete_preserves_other_items(self):
        targets = between_routing(self.board, [self.a, self.b])
        self.branch.SetSelected()
        apply_targets(self.board, targets, select=True)
        self.assertEqual(self.keys(item for item in self.board.GetTracks()
                                   if item.IsSelected()), self.keys(self.main))
        apply_targets(self.board, targets)
        self.assertEqual(self.keys(self.board.GetTracks()),
                         self.keys([self.branch, self.island, self.unrelated]))
        self.assertEqual(len(self.board.GetFootprints()), 2)

    def test_arc_path(self):
        self.board.RemoveNative(self.main[1])
        arc = pcbnew.PCB_ARC(self.board)
        arc.SetStart(position(5, 0))
        arc.SetMid(position(7.5, -2.5))
        arc.SetEnd(position(10, 0))
        arc.SetWidth(pcbnew.FromMM(0.2))
        arc.SetLayer(pcbnew.F_Cu)
        arc.SetNet(self.net)
        self.board.Add(arc)
        self.assertEqual(self.keys(between_routing(self.board, [self.a, self.b])),
                         self.keys([self.main[0], arc]))

    def test_dialog_preselection_and_select(self):
        self.a.SetSelected()
        self.b.SetSelected()
        dialog = UnrouteDialog(self.board)
        try:
            self.assertEqual(dialog.mode.GetSelection(), 2)
            self.assertEqual(self.keys(dialog.targets), self.keys(self.main))
            dialog.action.SetSelection(1)
            dialog.update_summary()
            self.assertEqual(dialog.delete.GetLabel(), "Select routing")
        finally:
            dialog.Destroy()

    def test_path_algorithm_against_brute_force(self):
        # Exhaustively check all undirected graphs with five vertices.
        pairs = [(i, j) for i in range(5) for j in range(i + 1, 5)]
        for mask in range(1 << len(pairs)):
            graph = {str(i): set() for i in range(5)}
            for bit, (i, j) in enumerate(pairs):
                if mask & (1 << bit):
                    graph[str(i)].add(str(j))
                    graph[str(j)].add(str(i))
            expected = set()
            def walk(node, visited):
                if node == "4":
                    expected.update(visited)
                    return
                for other in graph[node] - set(visited):
                    walk(other, visited + [other])
            walk("0", ["0"])
            self.assertEqual(path_vertices(graph, {"0"}, {"4"}), expected)


if __name__ == "__main__":
    app = wx.App(False)
    unittest.main()

