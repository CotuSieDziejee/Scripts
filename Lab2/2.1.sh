#!/bin/bash
if [ $# -gt 0 ]
then
for file in $@
do
echo $file:
cat $file
echo
echo
done
else echo "PODAJ NAZWE PLIKU"
fi
