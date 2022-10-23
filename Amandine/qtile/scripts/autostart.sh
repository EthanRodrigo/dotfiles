#!/bin/sh

killall picom
picom --config=$HOME/.config/picom/picom.conf &

killall -q nm-applet
nm-applet &
