#!/bin/bash
echo "$(cat)" | grep 'bash' | sed 's/:.*//'
