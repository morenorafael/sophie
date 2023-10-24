"""Groups settings for Qtile."""

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from .keys import mod, keys

groups = [

    # Browser
    Group(
        '  ',
        position=1,
        layout='max',
    ),

    # Code
    Group(
        ' ',
        position=2,
        layout='max',
    ),

    # Terminal
    Group(
        '  ',
        position=3,
        layout='column',
    ),

    # Apps
    Group(
        '  ',
        position=4,
        layout='max',
    ),

    # Obsidian
    Group(
        '  ',
        position=5,
        layout='max',
        matches=[Match(title='Obsidian')],
        spawn='/home/rafael/Obsidian-1.4.14.AppImage'
    ),

    # Process
    Group(
        ' ',
        position=6,
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
