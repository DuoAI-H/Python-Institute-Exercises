palabra=""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    palabra += ch
print(palabra)
