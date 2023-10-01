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
                    # inactive='4C566A',
                    # fontsize=16,
                    # this_screen_border='ffffff'

                    fontsize=16,
                    margin=3,
                    padding=8,
                    borderwidth=1,
                    active='ECEFF4',
                    inactive='4C566A',
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border='D08770',
                    this_current_screen_border='81A1C1',
                    this_screen_border='2E3440',
                    other_current_screen_border='4C566A',
                    other_screen_border='4C566A',
                    disable_drag=True
                ),
                widget.Prompt(),
                widget.WindowName(),
                
                widget.TextBox(
                    "",
                    fontsize=30,
                    foreground='D08770',
                    background='2E3440',
                    padding=0
                    
                ),


                widget.CurrentLayout(
                    background='D08770'
                ),

                widget.TextBox(
                    "",
                    fontsize=30,
                    foreground='8FBCBB',
                    background='D08770',
                    padding=0
                    
                ),

                widget.Clock(
                    format="%I:%M %p",
                    background='8FBCBB'
                ),

                widget.TextBox(
                    "",
                    fontsize=30,
                    foreground='BF616A',
                    background='8FBCBB',
                    padding=0
                    
                ),

                widget.Battery(
                    format='{char} {percent:2.0%} {hour:d} h {min:02d} m',
                    background='BF616A',
                    discharge_char='󱟤 ',
                    charge_char='󱟦 ',
                ),

                widget.TextBox(
                    "",
                    fontsize=30,
                    foreground='B48EAD',
                    background='BF616A',
                    padding=0
                    
                ),

                widget.Bluetooth(
                    fmt='󰂱  {}',
                    hci='/dev_8F_E0_2F_49_7B_5E',
                    background='B48EAD'
                ),

                widget.TextBox(
                    "",
                    fontsize=30,
                    foreground='5E81AC',
                    background='B48EAD',
                    padding=0
                    
                ),

                widget.WidgetBox(
                    widgets=[
                        widget.Memory(
                            measure_mem='G',
                            background='5E81AC'
                        )
                    ],
                    text_closed='  ',
                    text_open='  ',
                    background='5E81AC'
                ),

                widget.TextBox(
                    "",
                    fontsize=30,
                    foreground='2E3440',
                    background='5E81AC',
                    padding=0
                    
                ),

                widget.Systray(),

                widget.Spacer(
                    length=10
                )
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background='#2E3440',
            border_width=0
        ),
    ),
]
