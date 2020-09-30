## ------------ moduly.py ------------

def zliczLinie(nazwa_pliku):
	count = len(open(nazwa_pliku,'rU').readlines())
	print(count)

def zliczZnaki(nazwa_pliku):
	count = len(open(nazwa_pliku,'rU').read())
	print(count)

def checker():
	if __name__ =='__main__':
		checker()


## ------------ 7.3.py ------------

import moduly

nazwa_pliku = input("Podaj nazwe pliku: ")

print("Ilosc linii: ")
moduly.zliczLinie(nazwa_pliku)
print("Ilosc znakow: ")
moduly.zliczZnaki(nazwa_pliku)
