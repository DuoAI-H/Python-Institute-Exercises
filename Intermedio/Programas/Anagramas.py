try:
    word = input('Ingrese una cadena: ')
    word2 = input('Ingrese el anagrama: ')
    assert word.strip() != "" or word2.strip() != ""
except AssertionError:
    print('Los espacios no son anagramas')
    exit()
except :
    print('Ha ocurrido un error')
    exit()

word = word.replace(" ","").upper()
word2 = word2.replace(" ","").upper()

a=True
lon1 = len(word)
lon2 = len(word2)

if lon1 != lon2:
    print("No son Anagramas")
else:
    for i in word:
        if i not in word2:
            a = False

if a:
    print('Anagrama')
else:
    print("No son Anagramas")