#!/bin/bash

sed -r 's/^(.*? |)[^@]+@[^ ]+/\1nobody@example.com/g' mail.txt | tee mail.txt
