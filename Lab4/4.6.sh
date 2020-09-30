#!/bin/bash

awk -F ";" '{print "student="$1" " "\nocena="$NF "\nindeks="$2 " "}' oceny.txt
