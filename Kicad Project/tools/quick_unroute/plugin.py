"""Quick Unroute: a small KiCad 10 PCB Editor action plugin."""
import pcbnew
import wx
from .paths import path_vertices


def between_routing(board, footprints, allowed_nets=None):
    if len(footprints) != 2:
        return []
    shared = component_nets([footprints[0]]) & component_nets([footprints[1]])
    if allowed_nets is not None:
        shared &= allowed_nets
    if not shared:
        return []
    connectivity = board.GetConnectivity()
    connectivity.Build(board)
    items = list(board.GetTracks())
    items.extend(pad for fp in board.GetFootprints() for pad in fp.Pads())
    items = {item.m_Uuid.AsString(): item for item in items
             if item.GetNetCode() in shared}
    graph = {key: set() for key in items}
    def points(item):
        if isinstance(item, pcbnew.PAD):
            return [item.GetPosition()]
        return [item.GetStart(), item.GetEnd()]

    copper_layers = [layer for layer in board.GetEnabledLayers().Seq()
                     if pcbnew.IsCopperLayer(layer)]
    # Model junctions explicitly. A track-to-track graph would incorrectly include
    # dead-end branches because all tracks touching one junction form a clique.
    for key, item in items.items():
        neighbours = list(connectivity.GetConnectedTracks(item))
        neighbours.extend(connectivity.GetConnectedPads(item))
        neighbours = [other for other in neighbours
                      if other.m_Uuid.AsString() in items and
                      other.GetNetCode() == item.GetNetCode()]
        anchors = points(item)
        for other in neighbours:
            anchors.extend(point for point in points(other) if item.HitTest(point))
        layers = [layer for layer in copper_layers if item.IsOnLayer(layer)]
        for point in anchors:
            for layer in layers:
                junction = f"junction:{item.GetNetCode()}:{layer}:{point.x}:{point.y}"
                graph.setdefault(junction, set()).add(key)
                graph[key].add(junction)
    terminals = [{pad.m_Uuid.AsString() for pad in fp.Pads()
                  if pad.GetNetCode() in shared} for fp in footprints]
    keys = path_vertices(graph, *terminals)
    return [items[key] for key in keys if key in items and
            isinstance(items[key], pcbnew.PCB_TRACK)]


def component_nets(footprints):
    return {pad.GetNetCode() for fp in footprints for pad in fp.Pads()
            if pad.GetNetCode() > 0}


def connected_routing(board, footprints):
    """Walk physical track/via/pad connections; do not traverse zones."""
    connectivity = board.GetConnectivity()
    connectivity.Build(board)
    pending = [pad for fp in footprints for pad in fp.Pads()
               if pad.GetNetCode() > 0]
    seen = set()
    routing = {}
    while pending:
        item = pending.pop()
        key = item.m_Uuid.AsString()
        if key in seen:
            continue
        seen.add(key)
        if isinstance(item, pcbnew.PCB_TRACK):
            routing[key] = item
        neighbours = list(connectivity.GetConnectedTracks(item))
        neighbours.extend(connectivity.GetConnectedPads(item))
        pending.extend(other for other in neighbours
                       if other.GetNetCode() == item.GetNetCode())
    return list(routing.values())


def find_targets(board, net_codes=None, footprints=None, connected=False,
                 include_locked=False):
    if connected:
        candidates = connected_routing(board, footprints or [])
    else:
        candidates = [item for item in board.GetTracks()
                      if item.GetNetCode() in (net_codes or set())]
    return [item for item in candidates if include_locked or not item.IsLocked()]


def apply_targets(board, targets, select=False):
    if select:
        for item in list(board.GetTracks()) + list(board.GetFootprints()):
            item.ClearSelected()
        for footprint in board.GetFootprints():
            for pad in footprint.Pads():
                pad.ClearSelected()
        for item in targets:
            item.SetSelected()
    else:
        # KiCad's ActionPlugin runner records this as an undoable action.
        for item in targets:
            board.RemoveNative(item)
        board.GetConnectivity().Build(board)


class UnrouteDialog(wx.Dialog):
    def __init__(self, board):
        super().__init__(None, title="Quick Unroute", size=(640, 630),
                         style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.board = board
        self.targets = []
        self.mode = wx.RadioBox(self, label="Routing for", choices=[
            "Net", "Component(s)", "Between two components"],
            majorDimension=3, style=wx.RA_SPECIFY_COLS)
        self.search = wx.SearchCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.search.SetDescriptiveText("Filter net names or component references")
        self.picker = wx.ListBox(self, style=wx.LB_EXTENDED)
        self.scope = wx.Choice(self, choices=[
            "Only copper physically connected to component pads",
            "All routing on every net used by component pads"])
        self.scope.SetSelection(0)
        self.between_net = wx.Choice(self, choices=["All shared nets"])
        self.between_net.SetSelection(0)
        self.between_codes = [None]
        self.action = wx.Choice(self, choices=["Delete routing", "Select routing"])
        self.action.SetSelection(0)
        self.locked = wx.CheckBox(self, label="Also delete locked tracks/vias")
        self.note = wx.StaticText(self, label=(
            "Tracks, arcs and vias only. Pads, footprints and zones stay.\n"
            "Physical connections follow tracks/vias/pads, not zone fills.\n"
            "Use Ctrl/Shift to select multiple entries."))
        self.summary = wx.StaticText(self)
        buttons = wx.StdDialogButtonSizer()
        self.delete = wx.Button(self, wx.ID_OK, "Delete routing")
        buttons.AddButton(self.delete)
        buttons.AddButton(wx.Button(self, wx.ID_CANCEL))
        buttons.Realize()
        layout = wx.BoxSizer(wx.VERTICAL)
        for control in [self.mode, self.search, self.picker, self.scope,
                        self.between_net, self.action,
                        self.locked, self.note, self.summary]:
            layout.Add(control, 1 if control is self.picker else 0,
                       wx.EXPAND | wx.ALL, 8)
        layout.Add(buttons, 0, wx.ALIGN_RIGHT | wx.ALL, 8)
        self.SetSizer(layout)
        self.SetMinSize((640, 600))
        self.entries = []
        self.footprints = sorted(board.GetFootprints(),
                                 key=lambda fp: fp.GetReference().casefold())
        selected_fp = [fp for fp in self.footprints if fp.IsSelected()]
        selected_nets = {item.GetNetCode() for item in board.GetTracks()
                         if item.IsSelected() and item.GetNetCode() > 0}
        selected_nets.update(pad.GetNetCode() for fp in self.footprints
                             for pad in fp.Pads()
                             if pad.IsSelected() and pad.GetNetCode() > 0)
        self.mode.SetSelection(2 if len(selected_fp) == 2 else 1 if selected_fp else 0)
        self.mode.Bind(wx.EVT_RADIOBOX, self.populate)
        self.search.Bind(wx.EVT_TEXT, self.populate)
        self.picker.Bind(wx.EVT_LISTBOX, self.update_summary)
        self.scope.Bind(wx.EVT_CHOICE, self.update_summary)
        self.between_net.Bind(wx.EVT_CHOICE, self.update_summary)
        self.action.Bind(wx.EVT_CHOICE, self.update_summary)
        self.locked.Bind(wx.EVT_CHECKBOX, self.update_summary)
        self.delete.Bind(wx.EVT_BUTTON, self.confirm)
        self.populate()
        for index, (_, value) in enumerate(self.entries):
            if (self.mode.GetSelection() != 0 and value in selected_fp) or (
                    self.mode.GetSelection() == 0 and value in selected_nets):
                self.picker.SetSelection(index)
        self.update_summary()
        self.Centre()

    def populate(self, event=None):
        previous = {self.entries[i][0] for i in self.picker.GetSelections()}
        component_mode = self.mode.GetSelection() != 0
        self.scope.Enable(self.mode.GetSelection() == 1)
        self.between_net.Enable(self.mode.GetSelection() == 2)
        query = self.search.GetValue().casefold()
        if component_mode:
            entries = [(f"{fp.GetReference()}  —  {fp.GetValue()}", fp)
                       for fp in self.footprints]
        else:
            entries = sorted([(str(net.GetNetname()), net.GetNetCode())
                              for net in self.board.GetNetsByNetcode().values()
                              if net.GetNetCode() > 0],
                             key=lambda entry: entry[0].casefold())
        self.entries = [entry for entry in entries if query in entry[0].casefold()]
        self.picker.Set([entry[0] for entry in self.entries])
        for i, (label, _) in enumerate(self.entries):
            if label in previous:
                self.picker.SetSelection(i)
        self.update_summary()

    def update_summary(self, event=None):
        values = [self.entries[i][1] for i in self.picker.GetSelections()]
        mode = self.mode.GetSelection()
        component_mode = mode != 0
        nets = component_nets(values) if component_mode else set(values)
        if mode == 2:
            nets = (component_nets([values[0]]) & component_nets([values[1]])
                    if len(values) == 2 else set())
            previous_index = self.between_net.GetSelection()
            previous = self.between_codes[previous_index] if previous_index >= 0 else None
            codes = sorted(nets, key=lambda code: str(self.board.FindNet(code).GetNetname()))
            self.between_codes = [None] + codes
            self.between_net.Set(["All shared nets"] + [
                str(self.board.FindNet(code).GetNetname()) for code in codes])
            self.between_net.SetSelection(self.between_codes.index(previous)
                                          if previous in self.between_codes else 0)
            chosen = self.between_codes[self.between_net.GetSelection()]
            if chosen is not None:
                nets = {chosen}
            self.targets = between_routing(self.board, values, nets)
            if not self.locked.GetValue():
                self.targets = [item for item in self.targets if not item.IsLocked()]
        else:
            self.targets = find_targets(
                self.board, nets, values if component_mode else None,
                connected=component_mode and self.scope.GetSelection() == 0,
                include_locked=self.locked.GetValue())
        vias = sum(isinstance(item, pcbnew.PCB_VIA) for item in self.targets)
        verb = "delete" if self.action.GetSelection() == 0 else "select"
        self.delete.SetLabel(f"{verb.capitalize()} routing")
        self.summary.SetLabel(
            "Choose exactly two components." if mode == 2 and len(values) != 2 else
            f"{len(self.targets) - vias} tracks/arcs + {vias} vias to {verb}. "
            f"{len(nets)} net(s).")
        self.delete.Enable(bool(self.targets))

    def confirm(self, event):
        self.update_summary()
        if not self.targets:
            return
        if self.action.GetSelection() == 1:
            self.EndModal(wx.ID_OK)
            return
        names = sorted({str(item.GetNetname()) for item in self.targets})
        detail = "\n".join(names[:15])
        if len(names) > 15:
            detail += f"\n… and {len(names) - 15} more nets"
        whole_nets = (self.mode.GetSelection() == 0 or
                      self.mode.GetSelection() == 1 and self.scope.GetSelection() == 1)
        warning = ("\nThis removes routing across the entire selected nets, "
                   "including other components.\n" if whole_nets else "\n")
        answer = wx.MessageBox(
            f"Delete {len(self.targets)} tracks/arcs/vias?\n{warning}\n"
            f"Affected nets:\n{detail}\n\nUndo with Ctrl+Z in PCB Editor.",
            "Confirm routing deletion", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING,
            self)
        if answer == wx.YES:
            self.EndModal(wx.ID_OK)


class QuickUnroute(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Quick Unroute"
        self.category = "Routing"
        self.description = "Delete tracks/vias by net or component"
        self.show_toolbar_button = True

    def Run(self):
        board = pcbnew.GetBoard()
        if board is None:
            return
        dialog = UnrouteDialog(board)
        try:
            if dialog.ShowModal() == wx.ID_OK:
                apply_targets(board, dialog.targets,
                              select=dialog.action.GetSelection() == 1)
                pcbnew.Refresh()
        finally:
            dialog.Destroy()
