#!/bin/bash

awk 'match($0, /[12]?[0-9]?[0-9]\.[12]?[0-9]?[0-9]\.[12]?[0-9]?[0-9]\.[12]?[0-9]?[0-9]/) {print substr($0, RSTART, RLENGTH)}' adresy.txt | sort -r
