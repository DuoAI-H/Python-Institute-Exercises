# Demonstrando min() - Ejemplo 1
print(min("aAbByYzZ"))


# Demonstrando min() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Demostrando max() - Ejemplo 1
print(max("aAbByYzZ"))


# Demonstrando max() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# Demonstrando el método index()
# La ausencia del valor causara una excepcion
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demostrando la función list()
print(list("abcabc"))

# Demostrando el método count()
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Demostración del método capitalize()
print('aBcD'.capitalize())

# Demostración del método center()
print('[' + 'alfa'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

# Demostración del método endswith()
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

# Demostración del método find()
print("Eta".find("ta"))
print("Eta".find("mma"))
print('kappa'.find('a', 2))

txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)

#El tercer argumento apunta al primer indice que se
#tendra como limite de la busqueda

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

#Cualquier digito que no sea una letra o numero, es False
# Demostración del método the isalnum()
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

#Se interesa en letras solamente
# Ejemplo 1: Demostración del método isapha()
print("Moooo".isalpha())
print('Mu40'.isalpha())

#Se interesa solo en numeros
# Ejemplo 2: Demostración del método isdigit()
print('2018'.isdigit())
print("Año2019".isdigit())

# Ejemplo 1: Demostración del método islower()
print("Moooo".islower())
print('moooo'.islower())

# Ejemplo 2: Demostración del método isspace()
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Ejemplo 3: Demostración del método isupper() 
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demostración del método join()
print(",".join(["omicron", "pi", "rho"]))

# Demostración del método lower()
print("SiGmA=60".lower())

# Demostración del método the lstrip()
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))

# Demostración del método replace()
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
#Limita el numero de reemplazos
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

#Comienza la busqueda desde el final de la cadena
# Demostración del método rfind()
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# Demostración del método rstrip()
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# Demostración del método split()
print("phi       chi\npsi".split())

# Demostración del método startswith()
print("omega".startswith("meg"))
print("omega".startswith("om"))

# Demostración del método strip() 
print("[" + "   aleph   ".strip() + "]")

print("Yo sé que no sé nada.".swapcase())

# Demostración del método title()
print("Yo sé que no sé nada. Parte 1.".title())

# Demostración del método upper()
print("Yo sé que no sé nada. Parte 2.".upper())