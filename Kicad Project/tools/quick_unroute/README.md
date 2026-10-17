# Quick Unroute (KiCad 10)

Open **Tools → External Plugins → Quick Unroute**, or its toolbar button.

- Select a track/via/pad before opening to preselect its net.
- Select a footprint before opening to preselect the component.
- Otherwise, search and choose nets or component references in the dialog.
- Ctrl/Shift selects several entries.
- Select exactly two footprints before launching to open **Between two
  components** automatically. Or choose that mode and Ctrl-click two references.
  Choose all shared nets or one shared net, then **Select routing** or **Delete
  routing**. Includes alternate copper paths between their pads; excludes dangling
  branches and loops attached at only one junction. Vias on those paths are included.
  Paths may run through junctions/pads at other components on the same net.
  It cannot follow a path completed only by a zone fill, airwire, or component internals.
  Whole track/arc objects are selected/deleted; the plugin does not split segments.
- Component mode defaults to physically connected tracks/vias. It follows copper
  through tracks, arcs, vias and pads, but does not traverse filled zones or
  connections through component internals.
- The second component scope deletes all routing on its pad nets, board-wide.
  This can include shared ground/power routing and routing at other components.
- Locked items are skipped unless the checkbox is enabled.
- A confirmation lists the affected nets and item count. Ctrl+Z undoes deletion
  in the editor. The plugin never saves the board automatically.

Only tracks, copper arcs and vias are removed. Zones, pads and footprints remain.
After changing routing around zones, refill zones as usual (B).

## Installation

Copy this entire `quick_unroute` directory into KiCad's scripting plugin folder.
On this Windows installation that is:
`C:\Users\Aylon\AppData\Roaming\kicad\10.0\scripting\plugins`.
Then reload plugins in Preferences → Action Plugins, or restart PCB Editor.
For other systems, use the folder button in Preferences → Action Plugins.

Uses KiCad's bundled Python/wxPython; no extra packages. Built and tested with
KiCad 10.0.6. This is a legacy pcbnew ActionPlugin; KiCad plans to remove that
API in 11, so a future IPC port will be needed.

API reference: https://dev-docs.kicad.org/en/apis-and-binding/pcbnew/index.html
