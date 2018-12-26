# -----------------------------------------------------------------------------
# PROGRAMA   : ProblemaSuma2.0.py
# AUTOR      : Andre Iglesias
# DESCRIPCION: Mi quinto programa segunda version. Aprendiendo a programar.
# PROPOSITO  : Encuentra la suma de los números inscritos en un cuadrilatero 
# 			   rectangulo con el area mayor dentro de escaleras enumeradas.
# FECHA      : 09/04/2017
# -----------------------------------------------------------------------------

import time, sys, math


# Ordenar lista de derecha a izquierda
def Ordenamiento(M):
	Orden = [] 						# Crea una lista auxiliar
	for r in range(int(len(M))):
		# Comienza a añadir valores enteros decrecientemente a partir de la última posición de la lista a ordenar
		Orden.append(len(M)-(r+1))  
	M = [M[i] for i in Orden]		# Le asigna el orden a la lista según los valores de la lista auxiliar
	return M

# Imprime la escalera
def escalera():
	CR()
	lista = ['{:3}'.format(1)]		# Impide que para dígitos menores a 1000 de diferente magnitud, la escalera se deforme
	print("\n", lista)	
	for i in range(1,filita):
		lista = list(map(lambda x: '{:3}'.format(int(x)+i), lista)) # Impide que para dígitos menores a 1000 ...
		lista.insert(0,'{:3}'.format(int(lista[0])+1))
		time.sleep(0.1)				# Imprime la escalera con un tiempo deseado
		print("\n", lista)

# Calcula la suma de números inscritos en el cuadrilátero, imprime la matriz y sus elementos
def sumatoria(posicion,x):
	suma=0
	num=1
	for i in range(0,posicion):
		num+=i
		i+=1
	CR()
	# num tiene el valor del numero de la ultima columna, primera fila de la matriz

	# Asigna los valores de la matriz a la lista Matriz
	Matriz = [] 
	for r in range(posicion-x):
		for i in range(posicion):
			suma+=num
			i+1
			Matriz.insert(0,'{:3}'.format(num)) # Impide que para dígitos menores a 1000 ...
			num+=1

		num+=1+r
		Matriz.append(Matriz)
		del Matriz[-1]

	Matriz = Ordenamiento(Matriz) # Ordenar los valores de la matriz de menor a mayor

	#[Matriz[i] for i in Orden]

	Matriche = list(map(lambda x: int(x), Matriz)) # Regresando a tipo entero los valores de la lista

	Matriche2 = []

	lst = []

	GenMat(Matriche2,Matriche) # Lista de elementos enteros ordenados por fila en la matriz.

	GenMat(lst,Matriz) # Lista de elementos tipo cadena ordenados por fila en la matriz.

	Matriz = list(map(lambda x: int(x), Matriz)) # Regresando a tipo entero los valores de la lista

	
	print("Matriz: ", chr(27)+"[3;96m"+str(Matriche2)+chr(27)+"[0m") # Imprime Matriche2 en texto azul
	IMatriz(lst)	# Imprime la matriz de la escalera con la misma forma
	print("\nElementos de la matriz: ", chr(27)+"[3;93m"+str(Matriz)+chr(27)+"[0m") # Imprime Matriz en texto amarillo
	print("\nLa suma de los números inscritos en el cuadrilátero es: "+chr(27)+"[3;92m"+str(suma)+chr(27)+"[0m") # Imprime la suma de los
																												 # números de la matriz en texto verde
	return Matriz

# Imprime la matriz
def IMatriz(M):
#        print (' ', end=' ')
#        for i in range(len(M[1])):
#              print(i, end=' ')
        print('')
        print
        for i, element in enumerate(M):
        	# Letra Morada
            print(chr(27)+"[3;95m"+'{:3}'.format(i)+chr(27)+"[0m", chr(27)+"[1;39m"+"".join(str(element))+chr(27)+"[0m")

# Generador de matriz
def GenMat(L,M):
	if filita != 1:
		if filita%2 == 1:
			CGenMat(0,M,L) # Divide la lista M en sublistas según el orden de la escalera
		else:
			CGenMat(1,M,L) # Divide la lista M en sublistas según el orden de la escalera
	else:
		for i in range(int(len(M))):
			L.append(M[i*posicion:i*posicion+posicion])

# Complemento de GenMat
def CGenMat(r,M,L):
	for i in range(int(len(M))):
		Pos = i*(posicion+r)
		parte = Ordenamiento(M[Pos:Pos+posicion+r])
		L.append(parte)

		if i >= posicion+1:
			del L[-1]

	del L[-1]


# Carriage return <CR>, solo por presentacion)
def CR():
    print("\n")

# Asegura que el valor a leer sea del tipo que determine la llamada a esta función
def DesinfectanteDeTipo(prompt, tipo=None):

    while True:
        a = input(prompt)
        if tipo is not None:
            try:
                a = tipo(a)
            except ValueError:
                print("El valor debe ser de tipo {0}. ".format(tipo.__name__))
                continue
            else:
                return a
        else:
            return a

# Asegura un 'y' o un 'n' en la respuesta
def whl(prompt):
	while prompt.lower() not in {'n', 'y'}:
		prompt = input(chr(27)+"[3;91m"+"Digite un valor correcto. (Y/N) "+chr(27)+"[0m")
	return prompt

# -----------------------------------------------------------------------------
# MAIN BODY
# -----------------------------------------------------------------------------
CR()

CONDICION = input("¿Encontrar un la suma de los números inscritos en el cuadrilatero? (Y/N) ")

CR()

CONDICION = whl(CONDICION)

while CONDICION is "Y" or CONDICION is "y":

	filita=DesinfectanteDeTipo(chr(27)+"[1;39m"+"Digite número de fila: "+chr(27)+"[0m", tipo=int)
	escalera()

	if filita%2 == 0: 	# Si el numero de fila es un número par
		posicion=int(filita/2)	# La posicion se define así
		Matriz = sumatoria(posicion+1,1) # Si es par, restar 1 fila (segundo parámetro)

	else:				# Si el numero de fila es un número impar
		posicion=int((filita+1)/2) # La posicion se define así
		Matriz = sumatoria(posicion,0)	# Si es impar, restar 0 filas (segundo parámetro)

	CR()
	CONDICION = input("¿Encontrar más números inscritos? (Y/N) ")
	CONDICION = whl(CONDICION)

else:
    CR()
    print("Fin del programa.")
    CR()
