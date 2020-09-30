P = []
P = input("Podaj swój nr PESEL: ")


liczba_1 = 1*int(P[0])
while liczba_1 > 9:
  liczba_1 = liczba_1-10

liczba_2 = 3*int(P[1])
while liczba_2 > 9:
  liczba_2 = liczba_2-10

liczba_3 = 7*int(P[2])
while liczba_3 > 9:
  liczba_3 = liczba_3-10

liczba_4 = 9*int(P[3])
while liczba_4 > 9:
  liczba_4 = liczba_4-10

liczba_5 = 1*int(P[4])
while liczba_5 > 9:
  liczba_5 = liczba_5-10

liczba_6 = 3*int(P[5])
while liczba_6 > 9:
  liczba_6 = liczba_6-10

liczba_7 = 7*int(P[6])
while liczba_7 > 9:
  liczba_7 = liczba_7-10

liczba_8 = 9*int(P[7])
while liczba_8 > 9:
  liczba_8 = liczba_8-10

liczba_9 = 1*int(P[8])
while liczba_9 > 9:
  liczba_9 = liczba_9-10

liczba_10 = 3*int(P[9])
while liczba_10 > 9:
  liczba_10 = liczba_10-10

test = liczba_1 + liczba_2 + liczba_3 + liczba_4 + liczba_5 + liczba_6 + liczba_7 + liczba_8 + liczba_9 + liczba_10
while test>9:
  test=test-10

n=10-test

l = int(P[9])
if n == int(P[10]):
  print("PODANO PRAWDZIWY NUMER PESEL")
  print("Data urodzenia: " + P[4:6] + "-" + P[2:4] + "-" + P[0:2])
  if l==0 or l==2 or l==4 or l==6 or l==8:
    print("kobieta")
  else:
    print("mężczyzna")
else:
  print("PODANO ZŁY NUMER PESEL")