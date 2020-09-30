#!/bin/bash
if [ $# -eq 1 ]
then
name=$(date '+%H-%M %Y-%m-%d')
if test -e $1
then
$(tar -zvcf "$name.tar.gz" $1)
else
echo 'BLAD, KATALOG NIE ISTNIEJE'
fi
else
echo 'WYBIERZ KATALOG'
fi
