#!/bin/sh

if [[ $(pactl get-sink-mute @DEFAULT_SINK@ | awk '/no/ {print $2}') == "no" ]]; then
    pactl set-sink-mute @DEFAULT_SINK@ 1
else 
    pactl set-sink-mute @DEFAULT_SINK@ 0
fi
