## ------------ moduly.py ------------

def zliczLinie(nazwaPliku):
    count = len(open(nazwaPliku,'r').readlines())
    print(count)

def zliczZnaki(nazwaPliku):
    count = len(open(nazwaPliku,'r').read())
    print(count)

def znajdzNajdluzszaLinie(nazwaPliku):
    linia=max(open(nazwaPliku,'r').read().split(),key=len)
    plik=open(nazwaPliku,'r')
    numer=0
    for lin in plik:
        if(lin[0:-1]==linia):
            break
        numer+=1 
    print("Numer najdluzszej linii:",numer)
    print("Zawartosc najdluzszej linii:",linia)

def checker():
    if __name__ =='__main__':
        checker()

## ------------ 7.4.py ------------

nazwaPliku=input("Podaj nazwe pliku: ")
print("Linie:")
zliczLinie(nazwaPliku)
znajdzNajdluzszaLinie(nazwaPliku)