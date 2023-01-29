#!/bin/bash
clear
printf "This is information provided by mysystem.sh. Program starts now.\n\n"

printf "Hello, $USER\n\n"
printf "\n"

printf "Today's date is `date`, this week `date +"%V"`.\n\n"
printf "\n"

printf "These users are currently connected:\n"
w | cut -d "" -f l - | grep -v USER | sort -u
printf "\n"

printf "This is `uname -s` running on a `uname -m` processor.\n\n"
echo

printf "This is the uptime information:\n\n"
uptime
printf "\n"

printf "That's all folks!\n"
