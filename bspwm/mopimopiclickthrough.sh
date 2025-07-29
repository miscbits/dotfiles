#!/bin/bash

TARGET_NAME="MopiMopi - Vivaldi"

# Find the first window ID matching the window name
WIN_ID=$(xdotool search --name "$TARGET_NAME" | head -n 1)

if [ -z "$WIN_ID" ]; then
    echo "Window '$TARGET_NAME' not found."
    exit 1
fi

# Set _PICOM_TRANSPARENT_INPUT to 1 to enable clickthrough
xprop -id "$WIN_ID" -f _PICOM_TRANSPARENT_INPUT 8u -set _PICOM_TRANSPARENT_INPUT 1

echo "Clickthrough enabled for window ID $WIN_ID ('$TARGET_NAME')"
