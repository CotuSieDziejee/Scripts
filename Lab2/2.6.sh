#!/bin/bash
if test -f $1 && [ $# -gt 1 ]
then
for i in "$@"
do
if [ "$1" != "$i" ]
then
cp $1 $i
fi
done
else
echo "uzycie: ./zad.sh zr c1 c2 c3..."
fi
