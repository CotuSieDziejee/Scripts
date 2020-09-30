#!/bin/bash
if test -d "$1"
then
find "$1" -executable -type f -exec {} \;
else
echo "PODAJ NAZWE KATALOGU"
fi
