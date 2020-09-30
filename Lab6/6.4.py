import random

losowanie = (random.randint(0,10))

for i in range(5):
  strzal = int(input("Podaj liczbę od 0 do 10: "))
  if strzal == losowanie:
    print("WYGRAŁEŚ!!")
    break
  else:
    print("Przegrałeś :(")