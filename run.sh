#!/bin/bash

: '
This script uses exiftool to find the GPS Position of the provided file. 
If there is no file the program ends.
The outputs of the file are sent to a python script to calculate the coordinates as a decimal.
'

get_gps_coords() {
    if [[ -f "$1" ]]; then
        gps=$( exiftool $1 | grep "GPS Position" )
        if [[ -n "$gps" ]]; then
            # echo "$gps"
            # echo "running script python3 convert.py $gps"
            decimals=$( python3 convert.py $gps )
            echo "$decimals"
            # On Linux OS change pbcopy for `xclip -sel clip`
            echo "$decimals" | pbcopy
            
        else 
            echo "There was no GPS information in the file"
        fi
    else
        echo "Please append the file to your command"
    fi
}


get_gps_coords $1