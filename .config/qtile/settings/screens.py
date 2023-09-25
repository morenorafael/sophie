from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active='ECEFF4',
                    borderwidth=0,
                    inactive='4C566A',
                    fontsize=16,
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
                    foreground='BF616A',
                    background='D08770',
                    padding=0
                    
                ),

                widget.Clock(
                    format="%a %I:%M %p",
                    background='BF616A'
                ),

                widget.TextBox(
                    "",
                    fontsize=30,
                    foreground='2E3440',
                    background='BF616A',
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
