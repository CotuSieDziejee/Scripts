#!/bin/bash
if [ $# -eq 2 ]
then
if [ $1 -eq 1 ];
then
echo "$(cat -n $2)"
elif [ $1 -eq 2 ];
then
echo "$(cat -n $2 | tac)"
fi
else
echo "ARG, WARTOSC 1 - POCZATEK, 2 - KONIEC, ARG2 (PLIK TEKSTOWY)"
fi
