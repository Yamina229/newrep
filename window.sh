#!/bin/bash

# Ensure xdotool is installed
if ! command -v xdotool &> /dev/null; then
    echo "xdotool is required but not installed. Install it using 'sudo apt install xdotool'"
    exit 1
fi

# Step 1: Initial sleep and first click
sleep 2
xdotool mousemove 433 626 click 1
sleep 2

# Function to perform the "action" sequence
perform_action() {
    xdotool mousemove 150 39 click 1
    sleep 6
    xdotool mousemove 359 38 click 1
    sleep 6
    xdotool mousemove 590 39 click 1
    sleep 6
    xdotool mousemove 806 38 click 1
    sleep 6
    xdotool mousemove 1325 10 click 1
    sleep 2
}

# Perform "action" sequence the first time after the initial click
perform_action

# Array of locations to loop through
locations=(
    "519 628"
    "690 627"
    "687 628"
    "758 625"
    "850 627"
    "932 627"
    "1018 627"
    "1090 630"
    "1183 625"
)

# Loop through each location, click, then perform "action" sequence
for loc in "${locations[@]}"; do
    # Extract x and y coordinates from location
    x=$(echo $loc | cut -d' ' -f1)
    y=$(echo $loc | cut -d' ' -f2)

    # Click on the location and sleep for 2 seconds
    xdotool mousemove "$x" "$y" click 1
    sleep 2

    # Perform "action" sequence after each click
    perform_action
done
