# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

###########################################################################################################
# IMPORTS
###########################################################################################################
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.bar import Gap
from qtile_extras.widget import WiFiIcon
import subprocess, os, psutil

import sys
sys.path.insert(0, "~/.config/qtile/scripts")
from scripts.popupScript import showBatteryInfo, showCPUandMemoryGraph

###########################################################################################################
# SUPER KEY
###########################################################################################################
mod="mod4"


###########################################################################################################
# DEFAULT-SOFTWARE 
###########################################################################################################
terminal=guess_terminal()

@hook.subscribe.startup_once
def autostart():
    home=os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.Popen([home])

###########################################################################################################
# KEY-BINDINGS
###########################################################################################################

keys=[
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
    # Split=all windows displayed
    # Unsplit=1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # General
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Launch
    # tools
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # applications
    Key([mod, "shift"], "a", lazy.spawn("android-studio"), desc="Launch android studio"),
    Key([mod, "shift"], "b", lazy.spawn("brave"), desc="Launch brave"),
    Key([mod, "shift"], "d", lazy.spawn("discord"), desc="Launch discord"),
    Key([mod, "shift"], "n", lazy.spawn("notion-snap"), desc="Launch notion"),
    Key([mod, "shift"], "s", lazy.spawn("flatpak run com.spotify.Client"), desc="Launch notion"),
    Key([mod, "shift"], "t", lazy.spawn("flatpak run org.telegram.desktop"), desc="Launch notion"),
    # screenshot
    Key([], "Print", lazy.spawn("ksnip -f"), desc="Launch notion"),
    Key([mod], "Print", lazy.spawn("ksnip -r"), desc="Launch notion"),

    # Miscellaneous
    # Controlling the brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Controlling the sound
    # While using the bluetooth 
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ 1")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),

    # Just normal speackers
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("amixer sset 'Master' 5%+")),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("amixer sset 'Master' 5%-"))

]

###########################################################################################################
# COLORS
###########################################################################################################
colors = [
    ["#ecffe5"], ['#000'],
    ["#005266"], ['#00cdff'],
    ["#95eaff"], ['#cc00cc'],
    ['#ffff00'], ['#99ffcc'],
    ["#6666ff"], ['#4d4dff'],
    ['#9999ff'], ['#1a1aff'],
]

###########################################################################################################
# GROUPS
###########################################################################################################

groups = [Group(f"{i+1}", label="\uf111") for i in range(9)]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group=switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group=switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group=move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('mixer', 'pavucontrol', width=0.4,
             height=0.6, x=0.3, y=0.1, opacity=1),
    ], 
    single=False))
# extend keys list with keybinding for scratchpad
keys.extend([
    Key([], "F12", lazy.group['scratchpad'].dropdown_toggle('mixer'))
])

###########################################################################################################
# LAYOUTS
###########################################################################################################

layoutConfigs={
        "margin": 7,
        "border_width": 0,
        }

layouts=[
    layout.Columns(**layoutConfigs, fair=True, insert_position=1),
    layout.Max(**layoutConfigs),
    layout.MonadTall(**layoutConfigs, ratio=0.55), # one main page on left and others are on right
    layout.MonadWide(**layoutConfigs),
    layout.TreeTab(
        font="FreeMono",
        fontsize=20,
        **layoutConfigs,
        active_bg="#fff000", # the background color of the active tab
        active_fg="#00ffff", # the foreground color of the active tab 
        bg_color="#00f", # color of the pane
        inactive_bg="#dd4444", 
        inactive_fg="#ee1111",
        panel_width=200,
        section_fg="#aaa"
    ),
]


###########################################################################################################
# BAR
###########################################################################################################

# widgets
def getMemPercent():
    totalMem = psutil.virtual_memory().total / 1024 / 1024 / 1024
    usedMem = psutil.virtual_memory().used / 1024 / 1024 / 1024
    return str(int(usedMem / totalMem * 100)) + "%"

def initWidgets(visible_groups: list) -> list:
    widget_defaults=dict(
        font="sans",
        fontsize=12,
        padding=3,
    )
    extension_defaults=widget_defaults.copy()

    widgetList = [
        # First section
        widget.Image(
            filename="~/.config/qtile/assets/blackCornerLeft0.png",
            margin=0
        ),
        widget.Image(
            filename="~/.config/qtile/assets/archLogo.png",
            marrgin=0
        ),
        widget.Image(
            filename="~/.config/qtile/assets/blackCornerRight0.png",
            marrgin=0
        ),

        # Second section
        widget.CurrentLayoutIcon(
            background = colors[2],
            fontsize=20,
            scale=0.8
        ),
        # CurrentLayout text
        widget.CurrentLayout(
            background = colors[2],
            fontsize=21,
            font = 'Hurmit Nerd Font Mono'
            #font= 'JetBrains Mono Bold',
        ),
        widget.Image(
            filename="~/.config/qtile/assets/darkBlueCornerLeft.png",
            marrgin=0
        ),

        # Third section
        widget.GroupBox(
            disable_drag=True,
            background=colors[3],
            fontsize=28,
            active=colors[8],
            inactive=colors[7],
            block_highlight_text_color=colors[9],
            highlight_method="line",
            highlight_color=colors[10],
            borderwidth=2,
            urgent_alert_method="block",
            urgent_border=colors[11],
            visible_groups=visible_groups
        ),
        widget.Image(
            filename="~/.config/qtile/assets/lightBlueCornerRight.png",
            marrgin=0
        ),
        widget.Prompt(
            foreground=colors[0],
            background=colors[1],
            fontsize=28,
            font="FantasqueSansMono"
        ),
        widget.WindowName(
            background=colors[4],
            foreground=colors[5],
            fontsize=28,
            font="FantasqueSansMono"
        ),

        widget.Image(
            filename="~/.config/qtile/assets/heart.png",
            margin=0
        ),

        # Fourth section
        widget.Image(
            filename="~/.config/qtile/assets/lightBlueCornerLeft.png",
            margin=0
        ),

        # Volume
        widget.GenPollText(
            update_interval=1, 
            func=lambda: subprocess.check_output(os.path.expanduser('~/.config/qtile/scripts/volume.sh')).decode('utf-8'),
            fontsize=33,
            background=colors[3],
            foreground=colors[1]
        ),
        widget.PulseVolume(
            foreground=colors[1],
            background=colors[3],
            font = 'Hurmit Nerd Font Mono',
            fontsize=21
        ),

         # Bluetooth
        widget.GenPollText(
            update_interval=1,
            background=colors[3],
            func=lambda: subprocess.check_output(os.path.expanduser('~/.config/qtile/scripts/bluetooth.sh')).decode('utf-8'),
            font = 'Hurmit Nerd Font Mono',
            fontsize=21,
            foreground=colors[1]
        ),

        # Brightness
        widget.TextBox(
            " \uf185", 
            background=colors[3],
            foreground=colors[1],
            font = 'Hurmit Nerd Font Mono',
            fontsize=33
        ),
        widget.GenPollText(
            update_interval=0.2,
            background=colors[3],
            func=lambda: subprocess.check_output("brightnessctl | awk '{print $4}' | sed -n 2p | sed 's/(//' | sed 's/)//'", shell=True, text=True).split()[0], 
            foreground=colors[1],
            fontsize=21,
        ),

        # Wifi
        WiFiIcon(
            background=colors[3],
            interface="wlo1",
            fontsize=21,
            update_interval=0.2,
            inactive_colour=colors[0],
            active_colour=colors[1],
            foreground=colors[1],
        ),

        widget.Image(
            filename="~/.config/qtile/assets/darkBlueCornerRight.png",
            margin=0
        ),
 
        # Fifth section
        # Memory
        widget.TextBox(
            "\uf85a",
            background=colors[2],
            fontsize=30,
        ),

        widget.GenPollText(
            update_interval=0.2,
            func=getMemPercent, 
            background = colors[2],
            font = 'Hurmit Nerd Font Mono',
            fontsize=21,
            mouse_callbacks = {'Button1': lazy.function(showCPUandMemoryGraph)},
        ),

        #CPU
        widget.TextBox(
            "\uf2db",
            background=colors[2],
            fontsize=30,
        ),
        widget.CPU(
            background = colors[2],
            format='{load_percent}%',
            font = 'Hurmit Nerd Font Mono',
            fontsize=21,
            mouse_callbacks = {'Button1': lazy.function(showCPUandMemoryGraph)}
        ),

        # Battery
        widget.BatteryIcon(
            background = colors[2],
            mouse_callbacks = {'Button1': lazy.function(showBatteryInfo)},
        ),
        widget.Battery(
            format='{percent:2.0%}',
            fontsize=21,
            background = colors[2],
            font = 'Hurmit Nerd Font Mono',
        ),

        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),

        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),

       widget.Systray(
            background = colors[2],
            icon_size=25,
            padding=3
        ),

        widget.Image(
            filename='~/.config/qtile/assets/blackCornerRight1.png',
            margin=0,
        ),

        # Sixth section
        widget.Clock(
            format="\uf017 %H:%M", 
            fontsize=21,
            font='Source Code Variable',
            background=colors[1],
            foreground=colors[0],
            mouse_callbacks = {'Button1': lazy.spawn("osmo")},
        ),

        widget.Image(
            filename='~/.config/qtile/assets/blackCornerLeft1.png',
            margin=0
        ),
    ]
    return widgetList

# Multi monitor setup

def go_to_group(name: str):
    def _inner(qtile) -> None:
        if len(qtile.screens) == 1:
            qtile.groups_map[name].cmd_toscreen()
            return

        if name in '123':
            qtile.focus_screen(0)
            qtile.groups_map[name].cmd_toscreen()
        else:
            qtile.focus_screen(1)
            qtile.groups_map[name].cmd_toscreen()

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

def initSecondScreenBar():
    lst = initWidgets(['6', '7', '8', '9'])
    del lst[26]
    return lst

# screens
screens=[
    Screen(
        wallpaper="/home/dead/Pictures/firstScreen.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            widgets=initWidgets(['1', '2', '3', '4', '5']),
            size=30,
            background="#fff",
            margin=5,
        ),
        right=bar.Gap(5),
        left=bar.Gap(5),
        bottom=bar.Gap(5)
    ),
    Screen(
        wallpaper="/home/dead/Pictures/secondScreen.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            widgets=initSecondScreenBar(),
            size=25,
            background="#fff",
            margin=5,
        ),
        right=bar.Gap(5),
        left=bar.Gap(5),
        bottom=bar.Gap(5)
    )
]

###########################################################################################################
# MOUSE
###########################################################################################################

# Drag floating layouts.
mouse=[
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

###########################################################################################################
# MISCELLANEOUS
###########################################################################################################
dgroups_key_binder=None
dgroups_app_rules=[]  # type: list
follow_mouse_focus=True
bring_front_click=False
cursor_warp=False
floating_layout=layout.Floating(
    float_rules=[
        # Run the utility ofKB `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
#auto_fullscreen=True
focus_on_window_activation="smart"
reconfigure_screens=True
follow_mouse_focus=False # stops following the mouse

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize=True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules=None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname="LG3D"
