#!/bin/bash

# This script print a message about your weight if you give it your
# weight in kilo and height in centimeters.

weight="$1"
height="$2"
idealweight=$[$height - 110]

if [ $weight -le $idealweight ];
then
	echo "You should eat a bit more fat"
else
	echo "You should eat a bit more fruit."
fi

