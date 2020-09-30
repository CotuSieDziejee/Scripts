#!/bin/bash

awk -F "." 'length($1)<=8 && length($2)<=3 {print $1"."$2}' dos.txt
