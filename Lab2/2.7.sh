#!/bin/bash
nwd()
{
	l1=$1
	l2=$2

	reszta=$[$l1 % $l2]
	if [ $reszta -eq 0 ]
	then
	echo "NWD - $l2"
	else
	nwd $l2 $reszta
	fi
}
if [ $# -ne 2 ]
then
echo "PODAJ 2 ARGUMENTY DLA KTORYCH CHCESZ OBLICZYC RWD"
else
nwd $1 $2
fi
