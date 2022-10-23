#! /bin/bash

if [[ $(pactl get-sink-mute @DEFAULT_SINK@ 1| awk '{print $2}') == "yes" ]]; then
	icon="\ufa80"
elif [[ $(pactl get-sink-volume @DEFAULT_SINK@ | awk 'NR==1{print $5'}) != 0 ]]; then 
	icon="\uf028"
fi 

printf "$icon"
