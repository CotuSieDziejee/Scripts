plikWej="plik_wejsciowy"
plikWyj="plik_wyjsciowy"
zamiana=""

file=open(plikWej,"rb").read()

if (b'\r' in file):
    zamiana="Unix"

if(zamiana=="Unix"):
    liniePlik=file.replace(b'\r\n',b'\n')
else:
    zamiana = "Windows"
    liniePlik=file.replace(b'\n',b'\r\n')
    
print("Konwersja na",zamiana)
plik=open(plikWyj,"wb")
plik.write(liniePlik)
plik.close()