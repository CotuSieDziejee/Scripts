#!/bin/bash

awk -F "=" '{print $2}' oceny.txt | paste -d ";" - - -
