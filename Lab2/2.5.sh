#!/bin/bash
mll=$(cat)
echo "$mll" | cat > temp
awk '{ print length ()":" $0}' temp | sort -g | tail -n 1
