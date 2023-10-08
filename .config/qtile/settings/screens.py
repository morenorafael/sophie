from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    # active='ECEFF4',
                    # borderwidth=0,
                    # inactive='434C5E',
                    # fontsize=16,
                    # this_screen_border='ffffff'

                    fontsize=16,
                    margin=3,
                    padding=8,
                    borderwidth=1,
                    active='ECEFF4',
                    inactive='434C5E',
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border='D08770',
                    this_current_screen_border='81A1C1',
                    this_screen_border='2E3440',
                    other_current_screen_border='434C5E',
                    other_screen_border='434C5E',
                    disable_drag=True
                ),
                widget.Prompt(),

                widget.WindowName(),
                
                widget.TextBox(
                    "",
                    fontsize=55,
                    foreground='434C5E',
                    background='2E3440',
                    padding=-6
                ),


                widget.CurrentLayout(
                    background='434C5E',
                    foreground='B48EAD',
                    fmt='{}    '
                ),

                widget.Battery(
                    fmt='{}    ',
                    format='{char} {percent:2.0%} {hour:d} h {min:02d} m ',
                    background='434C5E',
                    foreground='8FBCBB',
                    discharge_char='  ',
                    charge_char=' ',
                    low_background='BF616A',
                    low_foreground='ECEFF4',
                    # low_percentage=0.5,
                ),

                widget.Bluetooth(
                    fmt='󰂱  {}    ',
                    hci='/dev_8F_E0_2F_49_7B_5E',
                    background='434C5E',
                    foreground='88C0D0'
                ),

                widget.Wlan(
                    fmt=' {}   ',
                    format='  {essid}  {percent:2.0%}',
                    interface='wlp61s0',
                    background='434C5E',
                    foreground='A3BE8C'
                ),

                widget.Memory(
                    fmt='  {}    ',
                    measure_mem='G',
                    background='434C5E',
                    foreground='EBCB8B'
                ),

                widget.Systray(
                    fmt=' {}',
                    background='434C5E',
                ),

                widget.Spacer(
                    length=10,
                    background='434C5E'
                ),

                widget.TextBox(
                    "  ",
                    foreground='ECEFF4',
                    background='434C5E',
                ),

                widget.Clock(
                    fmt=' {}',
                    format=' %I:%M %p',
                    background='434C5E',
                    foreground='ECEFF4'
                ),

                widget.Spacer(
                    length=10,
                    background='434C5E'
                )
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background='#2E3440',
            border_width=0
        ),
    ),
]
