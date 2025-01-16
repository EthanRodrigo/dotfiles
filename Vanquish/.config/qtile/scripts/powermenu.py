from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import(
    PopupRelativeLayout,
    PopupText
)

def powerMenu(qtile):
    configs = {
        "font": "Silkscreen"
    }
    
    controls = [
        PopupText(
            text="",
            fontsize= 75,
            pos_x=0.05,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("dm-tool lock")
            },
            **configs
        ),
        PopupText(
            text="",
            fontsize= 75,
            pos_x=0.32,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("systemctl suspend")
            },
            **configs
        ),
        PopupText(
            text="",
            fontsize= 75,
            pos_x=0.58,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("reboot")
            },
            **configs
        ),
        PopupText(
            text="",
            fontsize= 75,
            pos_x=0.88,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.spawn("shutdown now")
            },
            **configs
        ),
        PopupText(
            text="Lock",
            fontsize=20,
            pos_x=0,
            pos_y=0.7,
            width=0.15,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Sleep",
            fontsize=20,
            pos_x=0.25,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Reboot",
            fontsize=20,
            pos_x=0.52,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Shutdown",
            fontsize=20,
            pos_x=0.82,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background="00000060",
        initial_focus=None,
    )

    layout.show(centered=True)
