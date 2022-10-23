#!/bin/bash



if [[ "$(bluetoothctl show | grep 'Powered' | awk '{print $2}')" == "yes" ]] && [[ "$(bluetoothctl info)" == "Missing device address argument" ]]; then

    icon="\uf294 "

    connection="No device connected"

elif [[ "$(bluetoothctl show | grep 'Powered' | awk '{print $2}')" == "yes" ]] && [[ "$(bluetoothctl info)" != "Missing device address argument" ]]; then

    icon="\uf293 "

    connection="Device: $(bluetoothctl info | awk 'NR==2 {print $3}')"
    device="$(bluetoothctl info | awk 'NR==2 {print $3}')"

#    battery="Remaining battery: $(~/.local/bin/bluetooth_battery "$(bluetoothctl info | awk 'NR==1 {print $2}')" | awk '{print $6}')"

else

    icon="\uf5b1"

fi



case $BLOCK_BUTTON in

	1) setsid -f blueman-manager ;;

	3) notify-send "Bluetooth Module

$connection

$battery" ;;

esac



printf " $icon$device"
