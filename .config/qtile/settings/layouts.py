"""Layouts for Qtile"""

from libqtile import layout


layouts = [
    layout.Columns(
        border_focus='#56B6C2',
        border_focus_stack=["#56B6C2", "#56B6C2"],
        border_normal='#21252B',
        border_width=2,
        margin=2
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()
