import csv
import operator

file = 'osoby.csv'

person = []
class Person:
    person = []

    def __init__(self, nr, mail, rok_ur, imie):
        self.imie = imie
        self.rok_ur = rok_ur
        self.nr = nr
        self.mail = mail

    def __del__(self):
       print("")

    def Info_out(self):
        print("Numer : ", self.nr)
        print("E-mail: ", self.mail)
        print("Rok Urodzenia: ", self.rok_ur)
        print("Imie: ", self.imie)
    def dodajOsobe(self):
        linia = [self.nr, self.mail, self.rok_ur, self.imie]
        with open(file, 'a+', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            writer.writerow(linia)

    def sortujOsoby(column):
        sample = open('osoby.csv','r')

        csv1 = csv.reader(sample,delimiter=";")
        sort = sorted(csv1,key=operator.itemgetter(column))

        for eachline in sort:
            print(eachline)


def saveAsXML():
    try:
        file_name = 'osoby.csv'
        delimiter = ";"

        xmlF = file_name[:-4] +'.xml'

        with open(file_name, 'r') as csv_file:
            Data_from_csv = csv_file.readlines()

        tags = Data_from_csv.pop(0).strip().replace(' ', '_').split(delimiter)

        with open(xmlF, 'w') as xmlData:
            xmlData.write('<?xml version="1.0"?>\n')
            xmlData.write('<Osoby>\n')
            for row in Data_from_csv:
                rowData = row.strip().split(delimiter)
                xmlData.write('\t<Osoba>\n')
                for i in range(len(tags)):
                    xmlData.write('\t\t<' + tags[i] + '>' + rowData[i] + '</' + tags[i] + '>\n')

                xmlData.write('\t</Osoba>\n')
            xmlData.write('</Osoby>\n')
            print("Plik został zapisany jako .XML")
    except (IOError, ValueError):
        print("ERROR\n\n")
        saveAsXML()

def LoadFile():
    try:
        with open(file,newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in csv_reader:
                person.append(Person(row[0], row[1], row[2], row[3:]))
    except IOError:
        print("BLAD LADOWANIA PLIKU .CSV")
        exit()

def Person_out(numer):
    try:
        o[numer].Info_out()
    except IndexError:
        print("INDEX OVERFLOW")

def Person_add():
    try:
        imie = str(input("IMIE: "))
        nr = int(input("NUMER: "))
        rok = int(input("ROK UR: "))
        mail = str(input("EMAIL: "))

        osoba_add = Person(nr, mail, rok, imie)
        Person.dodajOsobe(osoba_add)
    except ValueError:
        print("Podano błędne dane")

def Person_sort(column):
    try:
        Person.sortujOsoby(column)
    except (ValueError, IndexError):
        print("Błąd (złe wartości / index)")


def Print_menu():
    print("\n\nMENU:")
    print("0. EXIT\n")
    print("1. Wypisz wszystkie osoby")
    print("2. Wypisz konkretną osobę")
    print("3. Posortuj osoby")
    print("4. Dodaj osobe")
    print("5. Zapisz jako .XML\n")


def Menu():
    option = int(input("Wywolaj opcje: "))

    try:
        if option == 0:
            exit()
        elif option == 1:
            try:
                for x in range(len(person)):
                    Person_out(x)
                    print()


            except IndexError:
                print("Przekroczono zakres, powrot do menu")

        elif option == 2:
            index = int(input("PODAJ INDEKS OSOBY: "))
            Person_out(index)

        elif option == 3:
            try:
                print("\n0. Numer")
                print("1. E-mail")
                print("2. Rok urodzenia")
                print("3. Imie")
                print("Wpisz numer odpowiadający kolumnie, według której chcesz wykonać sortowanie")
                column = int(input("Kolumna: "))
                Person_sort(column)

            except IndexError:
                print("Przekroczono zakres, powrot do menu")

        elif option == 4:
            print("DODAJ OSOBE DO LISTY\n")
            Person_add()

        elif option == 5:
            saveAsXML()

        else:
            print("Nie wybrano zadnego dostepnego menu, sprobuj ponownie")

    except (IOError, IndexError, ValueError):
        print("BŁĄD")


LoadFile()
o = []
for x in range(len(person)):
    o.append(person[x])

def tester():
    Print_menu()
    Menu()

if __name__ == '__main__':
    tester()
