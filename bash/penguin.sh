#!/usr/bin/env bash

#This script lets you present different menu to Tux. He will only be happy
# when given a fish.

if [ "$1" == fish ];
then
	echo "Hummmmmm Fish..... Tux happy!"
else
	echo "Tux don't like that. Tux wants fish"
fi
