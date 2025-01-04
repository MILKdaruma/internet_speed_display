#!/bin/bash
# SPDX-FileCopyrightText: 2024 Teruma Yamamoto <TRyamamototeruma@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

echo "Starting test script..."

cd $dir/ros2_ws || { echo "Error: Could not navigate to $dir/ros2_ws"; exit 1; }

echo "Building the workspace..."
colcon build 2> /dev/null || { echo "Error: Build failed"; exit 1; }
echo "Build completed."

echo "Sourcing ROS environment..."
source $dir/.bashrc
. install/setup.bash

echo "Launching the internet speed publisher node..."
timeout 60 ros2 run internet_speed_display internet_speed_publisher > /tmp/internet_speed.log &
PUBLISHER_PID=$!

for ((i = 1; i <= 60; i++)); do
    if ! ps -p $PUBLISHER_PID > /dev/null; then
        echo "Internet speed publisher node has terminated."
        break
    fi
    echo -ne "Running internet speed publisher... ($i/60 seconds)\r"
    sleep 1
done
wait $PUBLISHER_PID 2>/dev/null

if [[ $? -ne 0 ]]; then
    echo -e "\nWarning: Internet speed publisher node did not complete successfully."
else
    echo -e "\nInternet speed publisher node completed successfully."
fi

echo "Checking log output..."
grep 'Published:' /tmp/internet_speed.log && echo "Log check completed successfully." || echo "No matching log entries found."

echo "Test script finished."

