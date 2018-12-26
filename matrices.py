
# CHIO
def chio(matriz, multiplo = None):
    if multiplo is None: multiplo = 1
    if len(matriz) == 2:
        return multiplo*(matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0])
    else:
        ordenCuadrado = len(matriz[0])
        pivote = 0
        for i in matriz[0]:
            if i != 0:
                pivote = i
                break
        if pivote == 0: return 0
        else:
            multiplo *= -(1/(pivote**(ordenCuadrado-2))) if matriz[0].index(pivote)%2 != 0 else 1/(pivote**(ordenCuadrado-2))
            nueva = []
            for i in range(len(matriz)):
                if i != 0:
                    filanueva = []
                    for j in range(len(matriz[0])):
                        if j != matriz[0].index(pivote):
                            filanueva.append(pivote*matriz[i][j]-matriz[0][j]*matriz[i][matriz[0].index(pivote)])
                    nueva.append(filanueva)
            return int(chio(nueva, multiplo))


# Traza de matriz
def traza(matriz):
    acum = 0
    for i in range(len(matriz)):
        acum += matriz[i][i]
    return acum

# IMPRIME LA MATRIZ
def MOA(matriz, orden):
    for i in range(len(matriz)):

        print('|', end='')

        for j in range(len(matriz[i])):

            if j != (-1)%len(matriz[0]): print(matriz[i][j], end=' ')
            else: print(matriz[i][j], end='')

        if i != (-1)%len(matriz): print('|')
        else: print('| Ord. {}'.format(orden))


def inputM(prompt="Matriz: "):
    matriz = eval((str(input(prompt)).replace('{', '[')).replace('}', ']'))
    for i in range(len(matriz)):
        if len(matriz[i]) != len(matriz[(i+1)%len(matriz)]): quit()
    lenFila = len(matriz[0])
            
    if lenColumna != lenFila: orden = '{0} (rows) \u00D7 {1} (columns)'.format(lenColumna, lenFila)
    else: orden = str(lenFila)
    return matriz, chio(matriz)
                

#==========================================================================================================
# MAIN ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#==========================================================================================================
"""
matriz = inputM("Matriz: ")

# Longitudes de columnas y filas
lenColumna = len(matriz)
for i in range(len(matriz)):
    if len(matriz[i]) != len(matriz[(i+1)%len(matriz)]): quit()
lenFila = len(matriz[0])

if lenColumna != lenFila: orden = '{0} (rows) × {1} (columns)'.format(lenColumna, lenFila)
else: orden = str(lenFila)

MOA(matriz, orden)

# determinante de la matriz
# Chio
if orden == str(lenFila): print('\ndet. ', chio(matriz))
else: pass

print('traza ', traza(matriz))
"""
