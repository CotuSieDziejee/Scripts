#!/bin/bash
if [ $# -eq 2 ]
then
n=(5 2 1)
ile=$1
nominal=$2
if [ $ile -le $nominal ];
then
reszta=$[nominal - ile]
while [ $reszta -gt 0 ]
do
for i in ${n[@]}
do
if [ $reszta -ge $i ]
then
ilosc=$[reszta / $i]
reszta=$[reszta - $i*ilosc]
echo "$ilosc monet $i zł "
fi
done
if [ $reszta -eq 0 ];
then break;
fi
done
fi
fi
