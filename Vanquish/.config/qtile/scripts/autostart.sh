#!/bin/sh

if [[ -z "$(ps -a | grep picom)"  ]]; then
    picom --config=$HOME/.config/picom/picom.conf &
else
    killall picom
    picom --config=$HOME/.config/picom/picom.conf &
fi

killall -q nm-applet
nm-applet &

killall -q blueman-applet
blueman-applet &
