#!/bin/bash
if [ $# -ne 1 ] ; then
echo "PODAJ ROZMIAR TABLICY"
else
for (( w=1; w<=$1; ++w ))
do
for (( k=1; k<=$1; ++k ))
do
echo -n "$[$w*$k]	"
done
echo
done
fi
