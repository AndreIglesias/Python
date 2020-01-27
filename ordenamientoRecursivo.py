#!/opt/python3/bin/python3
def orden(lista, Aux = [], ayuda = None, minor = None, losPrimeros = None):
     if minor is None and lista != []:
             minor = int(lista[0])
             ayuda = lista
     if ayuda == []: return minor
     if len(Aux) == losPrimeros:
         return Aux
     else:
             if ayuda != None:
                 if int(minor) > ayuda[0]: minor = ayuda[0]
                 minor = orden(lista, Aux, ayuda[1:], minor, losPrimeros = losPrimeros)
     if minor != None and type(minor) == int:
         Aux.append(lista.pop(lista.index(minor)))
     return orden(lista, Aux, losPrimeros = losPrimeros)

print(orden([5,1,5,6,8,6,1,58,4,3], losPrimeros = 10))

# Ejercicios del examen

def prinmerEjercicio():
    print('TypeError')

def numeros():
    bandera = 0
    acum = 0
    x = int(input('Numero: '))
    i = 1
    while x > acum:
        acum += i**2
        if x == acum:
            print('si cumple')
            bandera = 1
        i += 1
    if bandera == 0: print('no cumple')
#numeros()

def temperatura():
    lista1 = ['hoy', 'manana', 'pasado']
    lista2 = ['temperatura']
    for i in lista1:
        if i[0]!='y':
            for j in lista2:
                print(j, end='')
    print('')
temperatura()


def Nombramiento():
    diccionario = {1:'uno', 2:'dos', 3:'tres', 4:'cuatro', 5:'cinco', 6:'seis', 7:'siete', 8:'ocho', 9:'nueve', 10:'diez', 20:'veinte', 30:'treinta',40:'cuarenta',50:'cincuenta',60:'sesenta',70:'setenta',80:'ochenta',90:'noventa',100:'ciento'}
    try:
        num = int(input('Numero: '))
        if num >= 16 and num <= 121:
            numero = []
            i = 0
            while num > 0:
                a = (num % 10)*(10**i)
                numero.insert(0,a)
                num //= 10
                i += 1
            for i in range(len(numero)):
                if i == len(numero) - 2: print(diccionario[numero[i]], 'y ', end = '')
                else: print(diccionario[numero[i]], end=' ')
    except ValueError: pass
#Nombramiento()

def palindrome(lista, auxiliar = []):
    if (len(lista) == len(auxiliar)) or (len(lista) == len(auxiliar) - 1):
        if (lista == auxiliar) or (lista == auxiliar[:-1]): return True
        else: return False
    else:
        auxiliar.append(lista.pop())
        return palindrome(lista, auxiliar)
print(palindrome([1,(1,2),3,(1,2),1]))

def Ordencito(tupla):
    try:
        for i in range(len(tupla)):
            if (i != len(tupla) - 1) and (tupla[i] > tupla[i+1]): return False
        return True
    except IndexError: pass
print(Ordencito((1,2,3,2,4,5)))

def matrice(matriz):
    nfil = len(matriz)
    ncol = len(matriz[0])
    for i in range(nfil):
        for j in range(ncol):
            if i == j: matriz[i][j] = 1
            else: matriz[i][j] = 0
matriz = [[1,2,3], [5,6,8], [5,5,6]]
matrice(matriz)
print(matriz)