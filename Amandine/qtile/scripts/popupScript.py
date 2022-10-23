from libqtile import widget
from qtile_extras.popup.toolkit import(
    PopupRelativeLayout,
    PopupWidget
)

def showBatteryInfo(qtile):
    widgetConfigs={
        "background": "#fff",
        "fontsize": 30,
        "foreground": "#ff5c33",
    }
    controls = [
        PopupWidget(
            widget=widget.BatteryIcon(
                **widgetConfigs,
            ),
            width=0.3,
            height=1,
            pos_x=0,
            pos_y=0
        ),

        PopupWidget(
            widget=widget.Battery(
                **widgetConfigs,
                charge_char="\uf583",
                empty_char="\uf244", 
                discharge_char="\uf584",
                full_char="\uf240",
                font="Hurmit NFM",
                format='{char} {percent:2.0%} \uf252 {hour:d}:{min:02d} \uf0e7 {watt:.2f} W'
            ),
            width=0.7,
            height=1,
            pos_x=0.5,
            pos_y=0
        )
    ]
    layout = PopupRelativeLayout(
        qtile,
        width=900,
        height=75,
        controls=controls,
        background="#fff",
        initial_focus=None,
        opacity=0.1
    )
    layout.show(x=int(qtile.current_screen.width / 2), y=50)
    
def showCPUandMemoryGraph(qtile):
    controls = [
        PopupWidget(
            widget=widget.MemoryGraph(),
            width=0.9,
            height=0.45,
            pos_x=0,
            pos_y=0
        ),
        PopupWidget(
            widget=widget.CPUGraph(),
            width=0.9,
            height=0.45,
            pos_x=0,
            pos_y=0.5
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=300,
        controls=controls,
        background="#000",
        initial_focus=None,
    )

    layout.show(x=int(qtile.current_screen.width / 2), y=50)
