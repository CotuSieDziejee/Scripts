import random

ilosc = int(input("PODAJ ILOŚĆ CIĄGÓW ZNAKÓW: "))
dlugosc = int(input("PODAJ DŁUGOŚĆ HASŁA: "))
i = 0
j = 0
haslo = ""
for j in range(ilosc):
  for i in range(dlugosc):
    litera = random.randint(21,126)
    haslo = haslo + chr(litera)
    i=i+1
  print("HASŁO: " + haslo)
  haslo = ""
  j = j + 1