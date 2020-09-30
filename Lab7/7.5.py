import random


File = []
Sentence = ""
WordsInFile = 0
WordsInSentence = 0


file=open("/usr/share/dict/words","r")
for word in file:
    File.append(word)
    WordsInFile += 1
file.close()

WordsInSentence = int(input("LICZBA SLOW W ZDANIU:"))

for i in range (0, WordsInSentence):
    word = File[random.randint(0, WordsInFile - 1)][0:-1]
    if (i == 0):
        word = word.capitalize()
    Sentence += word
    if (i < WordsInSentence - 1):
        Sentence += " "

Sentence += "."
print("\n")
print(Sentence)