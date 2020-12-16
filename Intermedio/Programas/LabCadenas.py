def misplit(strng):
    aux = ''
    lista = []
    ind = 0

    for ch in strng:
        if ch == ' ':
            if aux != '':
                lista.append(aux)
                aux = ''
            continue
        else:
            aux += ch
    return lista

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))
print(list("Ser o no ser, esa es la pregunta"))