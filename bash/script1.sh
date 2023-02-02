#!/usr/bin/env bash
# This script cclears the terminal, displays a greeting and gives information
# about currently connected users. The two example variales are set and displayed

clear							# clear terminal window

echo "The script starts now."

echo "Hi, $USER"					# dollar sign is used to get content of variable
echo

echo "I will now fetch you a list of connected users:"
echo
w							# sow who is logged on and
echo							# what they are doing

echo "I'm setting two variable now."
COLOUR="black"						# set a local shell variable
VALUE="9"						# set a local shell variable
echo "This is a string: $COLOUR"			# display content of variable
echo "And this is a number: $VALUE"			# display content of variable

echo "I'm giving you back your prompt now."
echo
