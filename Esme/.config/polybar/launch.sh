#!/usr/bin/env bash

#Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -x polybar >/dev/null; do sleep 1; done

# launching bar0
echo "---" | tee -a /tmp/bar0.log
polybar bar0 2>&1 | tee -a /tmp/bar0.log & disown

echo "Bars launched..."
