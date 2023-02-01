#!/bin/bash

# This script opens 4 terminal windows

i="0"

while [ "$i" -le 4 ]
do
xterm &
i=$[$i+1]
done

