plik = open('plik.txt','r')
S = plik.readlines()
dic={}
i=1;

for line in S:
	if dic.has_key(line):
		i = dic[line]
		i=i+1
		dic[line] = i
	else:
		dic[line] = i

print(dic)