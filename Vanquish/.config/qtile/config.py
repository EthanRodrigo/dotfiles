from libqtile import bar, layout, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from qtile_extras import widget
from qtile_extras.widget.decorations import GradientDecoration
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.groupbox2 import GroupBoxRule

import os, subprocess
import sys
sys.path.insert(0, "~/.config/qtile/scripts")
from scripts.health import showBatteryInfo, showHealth
from scripts.powermenu import powerMenu

mod = "mod4"
terminal = guess_terminal()

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.run([script])

####################################################################################################################################################
# KEYS 
####################################################################################################################################################
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod],"f",lazy.window.toggle_fullscreen(),desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # Launch Apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "b", lazy.spawn("brave"), desc="Launch Brave"),
    Key([mod, "shift"], "c", lazy.spawn("code"), desc="Launch Code"),
    Key([mod, "shift"], "d", lazy.spawn("flatpak run com.discordapp.Discord"), desc="Launch Discord"),
    Key([mod, "shift"], "s", lazy.spawn("flatpak run com.spotify.Client"), desc="Launch Spotify"),
    Key([mod, "shift"], "n", lazy.spawn("notion-snap-reborn"), desc="Launch Notion"),

    ## Controls 
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Audio 
    # Bluetooth
    #Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ 1")),
    Key([], "XF86AudioMute", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/mute.sh"), shell=True)),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),
    # Normal Speaker
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("amixer sset 'Master' 5%+")),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("amixer sset 'Master' 5%-")),

    # screenshot & cast
    Key([], "Print", lazy.spawn("ksnip -f"), desc="Screenshot a part of the screen"),
    Key([mod], "Print", lazy.spawn("ksnip -m"), desc="Screenshot the whole screen"),
    Key([mod, "shift"], "Print",  lazy.spawn("kazam"), desc="Screenshot the whole screen"),

    # Settings
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.function(powerMenu), desc="Prompt power menu"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]


# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

## Multi screen setup 
def go_to_group(name: str):
    def _inner(qtile) -> None:
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in '12345':
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()

    return _inner

for i in groups:
    if len(i.name) == 1:
        keys.append(Key([mod], i.name, lazy.function(go_to_group(i.name))))

keys.extend(
    [
    Key([mod, "mod1"], "1", lazy.window.toscreen(0)), 
    Key([mod, "mod1"], "2", lazy.window.toscreen(1)), 
    Key([mod, "control"], "n", lazy.next_screen()),
    ]
) 


####################################################################################################################################################
# LAYOUTS
####################################################################################################################################################

layoutConfigs={
    "margin":7,
    "border_width":0
}

layouts = [
    layout.Columns(
        **layoutConfigs,
        border_focus_stack=["#d75f5f", "#8f3d3d"],
    ),
    layout.Max(**layoutConfigs),
    layout.TreeTab(**layoutConfigs),
    layout.MonadTall(**layoutConfigs),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

####################################################################################################################################################
# BAR
####################################################################################################################################################

def initWidgets(visibleGroups: list) -> list:
    decorations = {
        "decorations": [
            GradientDecoration(
                whole_bar=True,
            ),
        ],
        "padding": 10,
    }

    widget_defaults = dict(
        padding=0,
        font='Space Mono'
    )
    extension_defaults = widget_defaults.copy()

    widgetList = [
        # Arch logo 
        widget.Image(
            filename='~/.config/qtile/assets/archLogo.png',
            margin=2,
            **decorations
        ),

        # Currunt Layout
        widget.CurrentLayoutIcon(
            scale=0.8,
            **decorations
        ),

        # The Groups 
        widget.GroupBox(
            fmt='',
            active='#ffffff',
            inactive='#000000',
            highlight_method="text",
            urgent_alert_method='block',
            urgent_text='#ff0000',
            margin=3,
            fontsize=23,
            disable_drag=True,
            visible_groups=visibleGroups,
            rules=[
                GroupBoxRule(text_colour="#00ffff").when(focused=False, occupied=True)
            ],
            **decorations,
        ),

        # Current Window
        widget.WindowName(
            font='Chakra Petch SemiBold',
            fontsize=23,
            margin=5,
            **decorations
        ),
        
        # Prompt
        widget.Prompt(
            font='Chakra Petch SemiBold',
            fontsize=23,
            margin=5,
            **decorations
        ),

        # Volume
        widget.PulseVolume(
            emoji=True,
            emoji_list=['', '', '', ''],
            fontsize=23,
            **decorations
        ),
        widget.Volume(
            fontsize=23,
            **decorations
        ),

        # Brightness
        widget.TextBox(
            "\uf185", 
            fontsize=23,
            **decorations
        ),
        widget.GenPollText(
            update_interval=0.2,
            func=lambda: subprocess.check_output("brightnessctl | awk '{print $4}' | sed -n 2p | sed 's/(//' | sed 's/)//'", shell=True, text=True).split()[0], 
            fontsize=23,
            **decorations
        ),

        #WiFi
        widget.WiFiIcon(
            fontsize=23,
            interface='wlo1',
            **decorations
        ),
        
        # Bluetooth
        widget.GenPollText(
            update_interval=1,
            func=lambda: subprocess.check_output(os.path.expanduser('~/.config/qtile/scripts/bluetooth.sh')).decode('utf-8'),
            fontsize=21,
            **decorations,
        ),
 
        # Laptop Health
        widget.TextBox(
            '',
            fontsize=23,
            mouse_callbacks = {'Button1': lazy.function(showHealth)},
            **decorations
        ),       
        # Systray
        widget.Systray(
            icon_size=25,
            **decorations
        ),
        
        # Battery
        widget.UPowerWidget(
            battery_height=13,
            mouse_callbacks = {'Button1': lazy.function(showBatteryInfo)},
            **decorations
        ),
    
        # Clock
        widget.Clock(
            font='Space Mono',
            fontsize=20,
            format="%H:%M", 
            **decorations
        ),

        # Power Menu
        widget.TextBox(
            '',
            foreground = '#ff0000',
            fontsize=23,
            mouse_callbacks = {'Button1': lazy.function(powerMenu)},
            **decorations
        )
    ]
    return widgetList

def initSecondScreen():
    lst = initWidgets(['6', '7', '8', '9'])
    del lst[12]
    return lst

screens = [
    Screen(
        wallpaper="/home/vanquish/Pictures/wallpaper0.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            widgets=initWidgets(['1', '2', '3', '4', '5']),
            size=30,
            margin=4,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
    Screen(
        wallpaper="/home/vanquish/Pictures/wallpaper1.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            widgets=initSecondScreen(),
            size=25,
            margin=5
        )
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
