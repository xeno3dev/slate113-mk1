"""Read-only smoke check on the real board; never saves or mutates its routing."""
from pathlib import Path
from time import perf_counter
from unittest.mock import patch
import pcbnew
import wx
with patch.object(pcbnew.ActionPlugin, "register"):
    from quick_unroute.plugin import between_routing, UnrouteDialog

app = wx.App(False)
board = pcbnew.LoadBoard(str(Path(__file__).resolve().parents[1] / "slate113.kicad_pcb"))
initial = len(board.GetTracks())
connectivity = board.GetConnectivity()
connectivity.Build(board)
pair = None
for track in board.GetTracks():
    pads = list(connectivity.GetConnectedPads(track))
    refs = {pad.GetParentFootprint().GetReference(): pad.GetParentFootprint()
            for pad in pads}
    if len(refs) >= 2:
        pair = list(refs.values())[:2]
        break
if pair:
    start = perf_counter()
    result = between_routing(board, pair)
    print("Real-board pair:", [fp.GetReference() for fp in pair],
          "routing items:", len(result), "seconds:", round(perf_counter() - start, 3))
    assert result
dialog = UnrouteDialog(board)
assert len(dialog.entries) > 0
dialog.Destroy()
assert len(board.GetTracks()) == initial
print("Real-board dialog/net list OK; routing unchanged:", initial)
