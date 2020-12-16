polEspDict = {
    "zamek" : "castillo",
    "kwiat" : "flor",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

elemento2 = polEspDict.get("woda")
print(elemento2)    # salida: agua

print(polEspDict["gleba"])