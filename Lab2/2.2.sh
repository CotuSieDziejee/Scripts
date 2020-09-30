#!/bin/bash
pliki=*.sh
for plik in $pliki
do
if head -n 1 $plik | grep -q '#!'
then
echo "PLIK $plik ZAWIERA ODWOLANIE DO INTERPRETERA"
if head -n 1 $plik | grep -q '#!/bin/bash'
then
echo "PLIK $plik - POPRAWNA SCIEZKA"
else
echo "PLIK $plik - NIEPOPRAWNA SCIEZKA"
fi
else
echo "PLIK $plik NIE ZAWIRA ODWOLANIA DO INTERPRETERA"
fi
done
