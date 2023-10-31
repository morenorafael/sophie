"""Screens configuration."""

import subprocess

from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy


def spacer(length=8, background='323842'):
    """Espacio entre widgets"""
    return widget.Spacer(length=length, background=background)


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=16,
                    margin=3,
                    padding=8,
                    borderwidth=1,
                    active='F6F7F9',
                    inactive='323842',
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border='D08770',
                    this_current_screen_border='56B6C2',
                    this_screen_border='21252B',
                    other_current_screen_border='323842',
                    other_screen_border='323842',
                    disable_drag=True
                ),

                widget.Prompt(),

                widget.WindowName(),

                widget.TextBox(
                    '',
                    fontsize=55,
                    foreground='323842',
                    background='21252B',
                    padding=-6
                ),

                widget.CurrentLayout(
                    fmt='   {}',
                    background='323842',
                    foreground='56B6C2',
                ),

                spacer(),

                widget.Battery(
                    fmt='{}',
                    format='{char}  {percent:2.0%}',
                    background='323842',
                    foreground='E06C75',
                    discharge_char='  ',
                    charge_char='󰂄  ',
                    low_background='E06C75',
                    low_foreground='D4D8DF',
                    low_percentage=0.2,
                ),

                spacer(),

                widget.Bluetooth(
                    fmt='󰂱 {}',
                    hci='/dev_8F_E0_2F_49_7B_5E',
                    background='323842',
                    foreground='88C0D0'
                ),

                spacer(),

                widget.Wlan(
                    fmt='   {}',
                    format='{essid} {percent:2.0%}',
                    interface='wlp61s0',
                    background='323842',
                    foreground='98C379'
                ),

                spacer(),

                widget.LaunchBar(
                    progs=[
                        ('/home/rafael/Pictures/spotify-icon.png', 'spotify-launcher', 'Spotify')
                        ],
                    icon_size=16,
                    padding_y=-1,
                    background='323842',
                ),

                spacer(length=1),

                widget.GenPollText(
                    fmt='{}',
                    update_interval=1,
                    func=lambda: subprocess
                    .check_output([
                        "/home/rafael/.local/bin/spotifycli", "--statusshort"
                        ])
                    .decode("utf-8")
                    .strip("\n"),
                    mouse_callbacks={
                        "Button1": lazy.spawn(
                            "/home/rafael/.local/bin/spotifycli --playpause"
                            ),
                    },
                    background='323842',
                    foreground='C678DD',
                ),

                spacer(),

                widget.Memory(
                    fmt='  {}',
                    measure_mem='G',
                    background='323842',
                    foreground='E5C07B'
                ),

                spacer(),

                widget.Backlight(
                    fmt='  {}',
                    backlight_name='intel_backlight',
                    background='323842',
                    foreground='61AFEF',
                ),

                spacer(),

                widget.PulseVolume(
                    fmt='   {}',
                    background='323842',
                    foreground='C678DD',
                    mouse_callbacks={
                        "Button1": lazy.spawn("pavucontrol"),
                    },
                ),

                spacer(),

                widget.Systray(
                    fmt='{}',
                    background='323842',
                ),

                spacer(),

                widget.Clock(
                    fmt='  {}',
                    format=' %I:%M %p',
                    background='323842',
                    foreground='D4D8DF'
                ),

                spacer(),

                widget.Clock(
                    fmt='  {}',
                    format='%d/%m/%Y',
                    background='323842',
                    foreground='56B6C2'
                ),

                spacer(),
            ],
            30,
            background='#21252B',
            border_width=0
        ),
    ),
]
