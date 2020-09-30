plik = open('plik.txt', 'r')

S = plik.readlines()
print("\nBefore:")
print(''.join(S))

S.sort(key=lambda s: s.split()[1])
print("After:")
print(''.join(S))