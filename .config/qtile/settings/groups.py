from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from .keys import mod, keys

groups = [

    # Browser
    Group(
        '  ',
        layout='max',
    ),

    # Code
    Group(
        ' ',
        layout='max',
    ),

    # Terminal
    Group(
        '  ',
        layout='column',
    ),

    # Apps
    Group(
        '  ',
        layout='max',
    ),

    # Process
    Group(
        ' ',
        layout='column',
    ),
]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])