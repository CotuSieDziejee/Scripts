wysokosc = int(input("PODAJ WYSOKOŚĆ TABLICZKI MNOŻENIA (y): "))
szerokosc = int(input("PODAJ SZEROKOŚĆ TABLICZKI MNOŻENIA (x): "))

for y in range(1,wysokosc):
     for x in range(1,szerokosc):
         print (x*y, end="\t")
     print()