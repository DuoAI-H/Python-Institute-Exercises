word = input("Ingrese una palabra: ")
word = word.upper()
sinVocal = ""

for i in range(len(word)):
    if word[i] == 'A' or word[i] == 'E'or word[i]=='I' or word[i]=='O'or word[i]=='U':
        continue
    sinVocal += word[i]
print(sinVocal)