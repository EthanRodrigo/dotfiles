#!/bin/bash

if [[ "$(bluetoothctl show | grep 'Powered' | awk '{print $2}')" == "yes" ]] && [[ "$(bluetoothctl info)" == "Missing device address argument" ]]; then
    icon="\uf294 "
    connection="No device connected"
else
    icon="\uf293 "
    connection="Device: $(bluetoothctl info | awk 'NR==2 {print $3}')"
    device="$(bluetoothctl info | awk 'NR==2 {print $3}')"
fi

printf " $icon$device"
