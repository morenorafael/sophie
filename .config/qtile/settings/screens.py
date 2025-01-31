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
                    # inactive='3E4452',
                    # fontsize=16,
                    # this_screen_border='ffffff'

                    fontsize=16,
                    margin=3,
                    padding=8,
                    borderwidth=1,
                    active='ECEFF4',
                    inactive='3E4452',
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border='D08770',
                    this_current_screen_border='56B6C2',
                    this_screen_border='282C32',
                    other_current_screen_border='3E4452',
                    other_screen_border='3E4452',
                    disable_drag=True
                ),

                widget.Prompt(),

                widget.WindowName(),
                
                widget.TextBox(
                    '',
                    fontsize=55,
                    foreground='3E4452',
                    background='282C32',
                    padding=-6
                ),

                widget.Spacer(
                    length=10,
                    background='3E4452'
                ),

                widget.CurrentLayout(
                    fmt='{}',
                    background='3E4452',
                    foreground='E06C75',
                ),

                widget.Spacer(
                    length=10,
                    background='3E4452'
                ),

                widget.Battery(
                    fmt='{}',
                    # format='{char}   {percent:2.0%} {hour:d} h {min:02d} m ',
                    format='{char}   {percent:2.0%} ',
                    background='3E4452',
                    foreground='98C379',
                    discharge_char=' ',
                    charge_char=' ',
                    low_background='BF616A',
                    low_foreground='ECEFF4',
                    low_percentage=0.2,
                ),

                widget.Spacer(
                    length=10,
                    background='3E4452'
                ),

                widget.Bluetooth(
                    fmt='󰂱  {}  ',
                    background='3E4452',
                    foreground='61AFEF'
                ),

                widget.Spacer(
                    length=10,
                    background='3E4452'
                ),

                widget.Wlan(
                    fmt='  {}',
                    format='  {essid}  {percent:2.0%}',
                    interface='wlan0',
                    background='3E4452',
                    foreground='C678DD',
                    use_ethernet=False
                ),

                widget.Net(
                    background='3E4452',
                    foreground='C678DD'
                ),

                widget.Spacer(
                    length=10,
                    background='3E4452'
                ),

                widget.Memory(
                    fmt=' {}',
                    measure_mem='G',
                    background='3E4452',
                    foreground='E5C07B'
                ),

                widget.Spacer(
                    length=10,
                    background='3E4452'
                ),

                widget.Backlight(
                    fmt=' {}',
                    backlight_name='intel_backlight',
                    background='3E4452',
                    foreground='98C379',
                ),

                widget.Spacer(
                    length=10,
                    background='3E4452'
                ),

                widget.PulseVolume(
                    fmt='   {}',
                    background='3E4452',
                    foreground='98C379',
                ),

                widget.Spacer(
                    length=10,
                    background='3E4452'
                ),

                widget.Systray(
                    fmt='   {}    ',
                    background='3E4452',
                ),

                widget.Spacer(
                    length=10,
                    background='3E4452'
                ),

                widget.Clock(
                    fmt='  {}',
                    format='%d/%m/%Y',
                    background='3E4452',
                    foreground='ECEFF4'
                ),

                widget.Clock(
                    # fmt='    {}   ',
                    format=' %I:%M %p',
                    background='3E4452',
                    foreground='ECEFF4'
                ),

                widget.Spacer(
                    length=15,
                    background='3E4452'
                )
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background='#282C32',
            border_width=0
        ),
    ),
]
