import numpy as np

def rSudoku(sudo):
    #Revisa si hay columnas repetivas
    for i in range(9):
        for j in range(1,9):
            if sudo[0][i] == sudo[j][i]:
                return False
    #Revisar si hay numeros reptidos dentro de las sub matrices
    for i in range (3,10,3):
        for j in range (3,10,3):
            #print(sudo[i-3:i,j-3:j])
            #print(np.unique(sudo[i-3:i,j-3:j]))
            if len(np.unique(sudo[i-3:i,j-3:j])) != 9:
                return False
    return True

#print("Digite las nueve filas del sudoku")

sudo = [0 for x in range(9)]
n = [1,2,3,4,5,6,7,8,9]
i=0


while 1:
    try:
        #Convierte una string a una list int
        sudo[i] = [int(x) for x in input('')]
        #Se asegura que mida 9 y que no se repitan numeros
        assert len(sudo[i])==9 and (n == sorted(sudo[i]))
    except AssertionError:
        print("La longitud no es igual a 9. Reescriba.")
        continue
    except ValueError:
        print("Error. Reescriba la fila 2")
        continue
    except:
        print("Ha ocurrido un error inesperado")
        exit()
    if i == 8:
        break
    i+=1

#Sudokus prueba, el primero devuelve True, el segundo False

"""
#Devuelve True si es un sudoku valido
sudo1 = [[2,9,5,7,4,3,8,6,1],
        [4,3,1,8,6,5,9,2,7],
        [8,7,6,1,9,2,5,4,3],
        [3,8,7,4,5,9,2,1,6],
        [6,1,2,3,8,7,4,9,5],
        [5,4,9,2,1,6,7,3,8],
        [7,6,3,5,2,4,1,8,9],
        [9,2,8,6,7,1,3,5,4],
        [1,5,4,9,3,8,6,7,2]]

sudo2 = [[1,9,5,7,4,3,8,6,2],
        [4,3,1,8,6,5,9,2,7],
        [8,7,6,1,9,2,5,4,3],
        [3,8,7,4,5,9,2,1,6], 
        [6,1,2,3,8,7,4,9,5],
        [5,4,9,2,1,6,7,3,8],
        [7,6,3,5,2,4,1,8,9],
        [9,2,8,6,7,1,3,5,4],
        [2,5,4,9,3,8,6,7,1]]

sudo1 = np.array(sudo1)
sudo2 = np.array(sudo2)
"""
sudo = np.array(sudo)
print(rSudoku(sudo))