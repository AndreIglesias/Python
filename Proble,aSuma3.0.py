# =============================================================================
# PROGRAMA   : ProblemaSuma3.0.py
# AUTOR      : Andre Iglesias
# DESCRIPCION: Mi quinto programa tercera version. Aprendiendo a programar.
# PROPOSITO  : Encuentra la suma de los números inscritos en un cuadrilatero 
# 	       rectangulo con el area mayor dentro de escaleras enumeradas.
# FECHA      : 10/04/2017
# =============================================================================


# _____________________________________________________________________________
# DECLARATIONS
# _____________________________________________________________________________


# -----------------------------------------------------------------------------
# VALIDATION FUNCTIONS
# -----------------------------------------------------------------------------

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
# VISUAL PRESENTATION
# -----------------------------------------------------------------------------

# Carriage return <CR>, solo por presentacion)
def CR():
    print("\n")

# -----------------------------------------------------------------------------
# MAIN FUNCTIONS
# -----------------------------------------------------------------------------


# Ordenar lista de derecha a izquierda
def Ordenamiento(M):
	Orden = [] 						# Crea una lista auxiliar
	for r in range(int(len(M))):
		# Comienza a añadir valores enteros decrecientemente a partir de la última posición de la lista a ordenar
		Orden.append(len(M)-(r+1))  
	M = [M[i] for i in Orden]		# Le asigna el orden a la lista según los valores de la lista auxiliar
	return M

# Lista int
def conversion(lst):
	lst = list(map(lambda x: int(x), lst))
	return lst

# Imprime la escalera con la matriz en azul
def matriz():
	sumita = 0
	if len(LISTA) > (posicion):
		print(chr(27)+"[96m"+str(LISTA[0:posicion])+chr(27)+"[0m", end=' ')
		print(LISTA[posicion:len(LISTA)])
		sumita += sum(conversion(LISTA[0:posicion]))

	elif len(LISTA) == (posicion):
		print(chr(27)+"[96m"+str(LISTA[0:posicion])+chr(27)+"[0m")
		sumita += sum(conversion(LISTA[0:posicion]))

	else:
		print(LISTA)

	return sumita

# _____________________________________________________________________________
# MAIN BODY
# _____________________________________________________________________________

CR()
CONDICION = input("¿Encontrar un la suma de los números inscritos en el cuadrilatero? (Y/N) ")
CR()

CONDICION = whl(CONDICION)

while CONDICION is "Y" or CONDICION is "y":

	lista, suma = [1], 0
	lista = list(map(lambda x: '{:3}'.format(x), lista)) # formato de x:'999'

	a = DesinfectanteDeTipo(chr(27)+"[1;39m"+"Numero de fila: "+chr(27)+"[0m", tipo = int)
	CR()

	if a%2 == 0: # si es par
		posicion = int(a/2)+1 # Total de filas pares contando fila 0
	else:
		posicion = int((a+1)/2) # Total de filas impares contando fila 1

	# La matriz solucion se imprime en azul dentro de la escalera
	if a == 1:
		print(chr(27)+"[96m"+str(lista)+chr(27)+"[0m") # Matriz 1x1 
		suma = 1
	else:
		print(lista)

	for i in range(1,a):
		lista = list(map(lambda x: int(x)+i, lista))
		lista.append(lista[-1]+1)
		lista = list(map(lambda x: '{:3}'.format(x), lista))
		LISTA = Ordenamiento(lista)
		suma += matriz()

	CR()
	print("La suma de los elementos de la matriz es: ", chr(27)+"[3;92m"+str(suma)+chr(27)+"[0m")

	CR()
	CONDICION = input("¿Encontrar más números inscritos? (Y/N) ")
	CONDICION = whl(CONDICION)
	CR()

else:
    CR()
    print("Fin del programa.")
    CR()
