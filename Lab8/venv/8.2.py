import csv
import operator
import lxml.etree as etree

class wczytaj_plik(object):
    def wczytaj(self):

        sample = open("osoby.csv","r")
        csv1 = csv.reader(sample,delimiter=";")

        for row in csv1:
            print (row)

class sortowanie:
    def sortowanie_numer(self):

        sample = open("osoby.csv", "r")
        csv1 = csv.reader(sample, delimiter=";")
        sort1 = sorted(csv1,key=operator.itemgetter(0))

        for row in sort1:
            print (row)


    def sortowanie_mail(self):

        sample = open("osoby.csv", "r")
        csv1 = csv.reader(sample, delimiter=";")
        sort2 = sorted(csv1,key=operator.itemgetter(1))

        for row in sort2:
            print (row)


    def sortowanie_rok(self):

        sample = open("osoby.csv", "r")
        csv1 = csv.reader(sample, delimiter=";")
        sort3 = sorted(csv1,key=operator.itemgetter(2))

        for row in sort3:
            print (row)


    def sortowanie_imie(self):

        sample = open("osoby.csv", "r")
        csv1 = csv.reader(sample, delimiter=";")
        sort4 = sorted(csv1,key=operator.itemgetter(3))

        for row in sort4:
            print (row)

class szukaj:
    def szukaj_numer(self):
        numer = input("podaj numer: ")

        sample = open("osoby.csv", "r")
        csv1 = csv.reader(sample, delimiter=";")

        for row in csv1:
            if numer in row[0]:
                print(row)

    def szukaj_mail(self):
        mail = input("podaj mail: ")

        sample = open("osoby.csv", "r")
        csv1 = csv.reader(sample, delimiter=";")

        for row in csv1:
            if mail in row[1]:
                print(row)

    def szukaj_rok(self):
        rok = input("podaj rok: ")

        sample = open("osoby.csv", "r")
        csv1 = csv.reader(sample, delimiter=";")

        for row in csv1:
            if rok in row[2]:
                print(row)

    def szukaj_imie(self):
        imie = input("podaj imie: ")

        sample = open("osoby.csv", "r")
        csv1 = csv.reader(sample, delimiter=";")

        for row in csv1:
            if imie in row[3]:
                print(row)



class dane:
    def dodaj(self):
        print("Podaj dane, które chcesz dodac")
        numer = input("Podaj numer: ")
        mail = input("Podaj adres e-mail: ")
        rok = input("Podaj rok urodzenia: ")
        imie = input("Podaj imie: ")

        pola = ['numer', 'mail', 'rok', 'imie']

        with open(r"osoby.csv","a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=pola)
            writer.writeheader()
            writer.writerow(
                {'numer':numer,
                 'mail':mail,
                 'rok':rok,
                 'imie':imie})


class Zamiana:
    # INITIALIZING XML FILE WITH ROOT IN PROPER NAMESPACE
    nsmap = {None: "http://WKI/Roughness-Profiles/1"}
    root = etree.Element('Roughness-Profiles', nsmap=nsmap)

    # READING CSV FILE
    with open("osoby.csv") as f:
        reader = csv.DictReader(f)

        # WRITE INITIAL XML NODES
        for row in reader:
            surface_elem = etree.SubElement(root, "surface", nsmap=nsmap)
            for elem_name, elem_value in row.items():
                etree.SubElement(surface_elem, elem_name.strip(), nsmap=nsmap).text = str(elem_value)

    # PARSE XSLT AND CREATE TRANSFORMER
    xslt_root = etree.parse("test.xsl")
    transform = etree.XSLT(xslt_root)

    # TRANSFORM
    #  (Note the weird use of tostring/fromstring. This was used so
    #   namespaces in the XSLT would work the way they're supposed to.)
    final_xml = transform(etree.fromstring(etree.tostring(root)))

    # WRITE OUTPUT TO FILE
    final_xml.write_output("test.xml")









x = wczytaj_plik()
y = sortowanie()
z = szukaj()
q = dane()
w = zamiana()

print("0 - Wyświetl plik    1 - Sortowanie (numer)    2 - Sortowanie (e-main)    3 - Sortowanie (rok)    4 - Sortowanie (imie)  ")
print("5 - Szukaj (numer)   6 - Szukaj (e-mail)   7 - Szukaj (rok)   8 - Szukaj (imie)   9 - Dodaj osobe   ")

opcja = int(input("Opcja nr: "))

if opcja == 0:
    x.wczytaj()
elif opcja == 1:
    y.sortowanie_numer()
elif opcja == 2:
    y.sortowanie_mail()
elif opcja == 3:
    y.sortowanie_rok()
elif opcja == 4:
    y.sortowanie_imie()
elif opcja == 5:
    z.szukaj_numer()
elif opcja == 6:
    z.szukaj_mail()
elif opcja == 7:
    z.szukaj_rok()
elif opcja == 8:
    z.szukaj_imie()
elif opcja == 9:
    q.dodaj()
elif opcja == 10:
    w()

else:
    print("BLAD!! ZLY NUMER!!")
