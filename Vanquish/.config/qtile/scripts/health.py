from libqtile import widget
from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import(
    PopupRelativeLayout,
    PopupWidget,
    PopupText
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
                format='{char} {percent:2.0%} \uf252 {hour:d}:{min:02d} \uf0e7 {watt:.2f} W', 
                notify_below = 10,
                padding = 3,
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
        opacity=0.5
    )
    layout.show(x=int(qtile.current_screen.width / 2), y=50)

def showHealth(qtile):
    controls = [
        PopupWidget(
            widget=widget.Memory(
                format='Memory: {MemPercent}%',
                measure_mem='G'
            ),
            width=0.2,
            height=0.3,
            pos_x=0,
            pos_y=0
        ),
        PopupWidget(
            widget=widget.MemoryGraph(),
            width=0.8,
            height=0.5,
            pos_x=0.2,
            pos_y=0
        ),
        PopupWidget(
            widget=widget.CPU(
                format='CPU: {load_percent}%',
            ),
            width=0.2,
            height=0.3,
            pos_x=0,
            pos_y=0.5
        ),
        PopupWidget(
            widget=widget.CPUGraph(),
            width=0.8,
            height=0.5,
            pos_x=0.2,
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
        opacity=0.7
    )
    layout.show(x=int(qtile.current_screen.width / 2), y=50)
