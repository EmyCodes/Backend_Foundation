#!/usr/bin/env bash

# This script print a message about your weight if you give it your
# weight in kilo and height in centimeters.

if [ ! $# == 2 ]; then
	echo "Usage: $0 weight_in_kilos length_in_centimeter"
	exit
fi

weight="$1"
height="$2"
idealweight=$((height - 110))

if [ "$weight" -le $idealweight ];
then
	echo "You should eat a bit more fat"
else
	echo "You should eat a bit more fruit."
fi

