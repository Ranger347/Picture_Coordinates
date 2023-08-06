#!/usr/bin/python3

# This program takes in values from the run.sh file and converts them into the 
# decimal forms of the coordinates.
# IE: inputs ## deg ##' ##.##" N/S, ## deg ##' ##.##" W/E
# outputs ##.####° N/S, ##.####° W/E

import argparse

def convert_to_decimal(degree, minute, second):
    return float(degree) + float(minute) / 60 + float(second) / 3600


parser = argparse.ArgumentParser(description='GPS coordinates to decimal')
parser.add_argument("gps", type=str, help='A string of GPS data from the bash script')
word, gps = parser.parse_known_args()
# print(gps)

north, west = convert_to_decimal(gps[2], gps[4][:-1], gps[5][:-1]), convert_to_decimal(gps[7], gps[9][:-1], gps[10][:-1])

print(f"{round(north, 4)}° {gps[6]} {round(west, 4)}° {gps[11]}")