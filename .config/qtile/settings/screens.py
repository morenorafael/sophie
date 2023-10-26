"""Screens configuration."""

import subprocess

from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    # active='ECEFF4',
                    # borderwidth=0,
                    # inactive='323842',
                    # fontsize=16,
                    # this_screen_border='ffffff'

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
                    fmt='{}\t',
                    background='323842',
                    foreground='56B6C2',
                ),

                widget.Battery(
                    fmt='{}\t',
                    # format='{char}   {percent:2.0%} {hour:d} h {min:02d} m ',
                    format='{char}   {percent:2.0%} ',
                    background='323842',
                    foreground='E06C75',
                    discharge_char=' ',
                    charge_char=' ',
                    low_background='E06C75',
                    low_foreground='D4D8DF',
                    low_percentage=0.2,
                ),

                widget.Bluetooth(
                    fmt='󰂱 {}\t',
                    hci='/dev_8F_E0_2F_49_7B_5E',
                    background='323842',
                    foreground='88C0D0'
                ),

                widget.Wlan(
                    fmt=' {}\t',
                    format='  {essid}  {percent:2.0%}',
                    interface='wlp61s0',
                    background='323842',
                    foreground='98C379'
                ),

                widget.GenPollText(
                    fmt=' {}\t',
                    update_interval=1,
                    func=lambda: subprocess
                    .check_output(["/home/rafael/.local/bin/spotifycli", "--statusshort"])
                    .decode("utf-8")
                    .strip("\n"),
                    mouse_callbacks={
                        "Button1": lazy.spawn("/home/rafael/.local/bin/spotifycli --playpause"),
                    },
                    background='323842',
                    foreground='C678DD',
                ),

                widget.Memory(
                    fmt=' {}\t',
                    measure_mem='G',
                    background='323842',
                    foreground='E5C07B'
                ),

                widget.Backlight(
                    fmt=' {}\t',
                    backlight_name='intel_backlight',
                    background='323842',
                    foreground='61AFEF',
                ),

                widget.PulseVolume(
                    fmt=' {}\t',
                    background='323842',
                    foreground='C678DD',
                    mouse_callbacks={
                        "Button1": lazy.spawn("pavucontrol"),
                    },
                ),

                widget.Systray(
                    fmt='{}\t',
                    background='323842',
                ),

                widget.Spacer(
                    length=10,
                    background='323842'
                ),

                widget.Clock(
                    fmt='  {}\t',
                    format='%d/%m/%Y',
                    background='323842',
                    foreground='56B6C2'
                ),

                widget.Clock(
                    fmt=' {}',
                    format=' %I:%M %p',
                    background='323842',
                    foreground='D4D8DF'
                ),

                widget.Spacer(
                    length=1,
                    background='323842'
                )
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background='#21252B',
            border_width=0
        ),
    ),
]
