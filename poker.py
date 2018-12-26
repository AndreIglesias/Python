"""
Materia	:	Matematicas Discretas 2
Titulo 	: 	Proyecto parte 2
Fecha	:	2017-11-16
Entrega	:	2017-11-23
Alumno	:	Andre :v
"""

import collections, itertools, operator, __future__
from functools import reduce
from random import randint
from copy import deepcopy


def combinations(k,r):
	if(min(r, k-r)>=0): r = min(r, k-r)
	if(k<r): return 0
	if(r==0): return 1
	return reduce(operator.mul, range(k, k-r, -1))//reduce(operator.mul, range(1, r+1))

class MetaClass(type):
	"""docstring for MetaClass"""
	@classmethod
	def __prepare__(metacls, name, bases, **kw):
		return collections.OrderedDict()

	def __new__(cls, name, bases, namespace, **kw):
		result = type.__new__(cls, name, bases, dict(namespace))
		result.members = tuple(namespace)
		result.verification = tuple(filter(lambda member: member[0] !="_", namespace))
		result.els = tuple(filter(lambda member: member[:2] == "_n", namespace))
		return result

class Baraja(metaclass=MetaClass):
	"""docstring for Baraja"""

	class _Cartas(collections.MutableMapping):
		"""docstring for _Cartas"""
		def __init__(self, num, palos, *args, **kw):
			super(collections.MutableMapping, self).__init__(*args, **kw) #self.__class__
			self.num = list(num)
			self.palos = list(palos)
			self.cantidadNumeros = dict(zip(self.num, [len(palos)]*len(self.num)))
			self.storage = dict(zip(self.palos, [deepcopy(list(num)), deepcopy(list(num)), deepcopy(list(num)), deepcopy(list(num))]))
			self.update(dict(*args, **kw))

		@property
		def jugadasPosibles(self): return combinations(len(self), 5)

		def __getitem__(self, key):
			try: return self.storage[self.__keytransform__(key)]
			except: 
				try:
					key = str(key).split(".")
					return self.storage[self.__keytransform__(key[1])][self.storage[self.__keytransform__(key[1])].index(int(key[0]))]
				except: raise KeyError("_Cartas")
		def __setitem__(self, key, value): 
			print(value)
			self.storage[self.__keytransform__(key)] = value
		def __delitem__(self, key): # -- corregir
			try: del self.storage[self.__keytransform__(key)]
			except:
				try:
					key = str(key).split(".") # del cartas['1.T']
					del self.storage[self.__keytransform__(key[1])][self.storage[self.__keytransform__(key[1])].index(int(key[0]))]
					self.cantidadNumeros[int(key[0])] -= 1
					# filtrar palos vacios
					if(self.storage[self.__keytransform__(key[1])]==[]):
						self.palos.pop(self.palos.index(key[1]))
				except: raise KeyError("_Cartas")

		def __iter__(self): return iter(self.storage)
		def __len__(self): return sum(tuple(map(lambda palo: len(self.storage[palo]), self.storage))) #sum(self.storage.values()) 
		def __repr__(self): return str(self.storage)
		def __keytransform__(self, key): return key

		def repetitions(self, r, mano, bandera = False): # r = cartas repetidas
			utilizado = 0
			if(bandera):
				Mano = tuple(map(lambda x: x[0], mano))
				for i in Mano:
					if Mano.count(i) == 2:
						utilizado = combinations(self.cantidadNumeros[i], r)
						break
			return sum(list(map(lambda k: combinations(k, r), self.cantidadNumeros.values())))-utilizado

		def diferentes(self, r, mano, algunasCartas = True, dobleP = False): # r = cartas diferentes
			lista = list(self.cantidadNumeros.values())
			if(algunasCartas):
				Mano = tuple(map(lambda x: x[0], mano))
				doble = False
				for i in Mano:
					if Mano.count(i) in {2,3,4}:
						try:
							lista.pop(lista.index(self.cantidadNumeros[i]))
						except:
							pass
						if(not dobleP): break
						elif(dobleP and doble): break
						doble = True
			return {
						1:sum(lista),
						2:sum(tuple(map(lambda tp: tp[0]*tp[1], itertools.combinations(lista,2)))),
						3:sum(tuple(map(lambda tp: tp[0]*tp[1]*tp[2], itertools.combinations(lista,3)))),
						4:sum(tuple(map(lambda tp: tp[0]*tp[1]*tp[2]*tp[3], itertools.combinations(lista,4)))),
						5:sum(tuple(map(lambda tp: tp[0]*tp[1]*tp[2]*tp[3]*tp[4], itertools.combinations(lista,5))))
					}[r] #switch

	#----------------------------------------------------------------------------------------------------


	def __init__(self, *args, **kw):
		super(Baraja, self).__init__(*args, **kw)
		self.cartas = self._Cartas(num = range(1,14), palos = ['P','T','R','C'])
		self.mano = self._genMano()

	"""
	Metodos de la clase Baraja
	"""

	def _genMano(self):
		barajaCopy = deepcopy(self.cartas)
		Mano = []
		palitos = barajaCopy.palos
		boolCont = 0
		while len(Mano) != 5:
			try:
				manjar = palitos[randint(0,len(palitos)-1)]
			except:
				break
				print(palitos, barajaCopy)
			if(len(barajaCopy[manjar])>1): carta = randint(0, len(barajaCopy[manjar])-1)
			else: carta = 0 
			if([] in barajaCopy.values() and boolCont != len(list(filter(lambda x: x==[], barajaCopy.values())))):
				palitos = list(filter(lambda x: barajaCopy[x]!=[], barajaCopy))
				boolCont += 1
			else:
				Mano.append((barajaCopy[manjar][carta], manjar)) 
				del barajaCopy[manjar][carta]
		Mano.sort()
		return Mano

	def _actualizar(self):

		for carta in self.mano:
			del self.cartas[str(carta[0])+'.'+carta[1]]
		self.mano = self._genMano()

	# ========================

	def _ccc(self): #concurrencia
		cartas = tuple(map(lambda x: x[0], self.mano))
		return tuple(map(lambda x: cartas.count(x),tuple(set(cartas))))

	def _color(self):
		for i in range(len(self.mano)-1):
			if(self.mano[i][1]!=self.mano[i+1][1]): return False
		return True

	def _escalera(self):
		if(self.mano[0][0]!=1 or self.mano[1][0]!=10):
			for i in range(len(self.mano)-1):
				if(self.mano[i][0]+1!=self.mano[i+1][0]): return False
			return True
		else:
			if(self.mano[1][0]==10 and self.mano[-1][0]==13): return True
			return False

	# +++

	def _kolor(self):
		return sum(tuple(map(lambda carta: combinations(len(carta), 5), self.cartas.storage.values())))/self.cartas.jugadasPosibles*10000000
	def _real(self):
		suma = 0
		for palo in self.cartas.storage.values():
			try: suma += int(palo[0]==1 and palo[-4]==10)
			except: pass
		return suma/self.cartas.jugadasPosibles*10000000

	def _e(self):
		r = 0
		for i in range(1,10):
			mult = 1
			for _ in range(5):
				mult *= self.cartas.cantidadNumeros[i+_]
			r += mult
		r += self.cartas.cantidadNumeros[1]*self.cartas.cantidadNumeros[10]*self.cartas.cantidadNumeros[11]*self.cartas.cantidadNumeros[12]*self.cartas.cantidadNumeros[13]
		return r/self.cartas.jugadasPosibles*10000000

	def _eColor(self):
			total = 0
			for palo in self.cartas:
				cont = 1
				entro = False
				for i in range(len(self.cartas[palo])-1):
					if(self.cartas[palo][i]+1==self.cartas[palo][i+1]): cont += 1
					else:
						entro = True
						if(cont>4):
							total += cont - 4
						cont = 0
				if(not entro):
					if(cont>4):
						total += cont - 4
			return total/self.cartas.jugadasPosibles*10000000

	def _dobleP(self):
		lista = list(self.cartas.cantidadNumeros.values())
		return sum(tuple(map(lambda tp: combinations(tp[0],2)*combinations(tp[1],2), itertools.combinations(lista,2))))*self.cartas.diferentes(1,self.mano,dobleP=True)/self.cartas.jugadasPosibles*10000000

	# ========================

	def pareja(self):
		if(self._ccc().count(2)==1 and self._ccc().count(3)==0):
			return self.cartas.repetitions(2,self.mano)*self.cartas.diferentes(3,self.mano)/self.cartas.jugadasPosibles*10000000

	def parejas(self):
		if(self._ccc().count(2)==2):
			return self._dobleP()

	def trio(self):
		if(self._ccc().count(2)==0 and self._ccc().count(3)==1):
			return self.cartas.repetitions(3,self.mano)*self.cartas.diferentes(2,self.mano)/self.cartas.jugadasPosibles*10000000

	def full(self):
		if(self._ccc().count(2)==1 and self._ccc().count(3)==1):
			return self.cartas.repetitions(2,self.mano)*self.cartas.repetitions(3,self.mano,True)/self.cartas.jugadasPosibles*10000000

	def poker(self):
		if(self._ccc().count(4)==1):
			return self.cartas.repetitions(4,self.mano)*self.cartas.diferentes(1,self.mano)/self.cartas.jugadasPosibles*10000000

	def escalera(self):
		if(self._escalera() and not (self.mano[0][0]==1 and self.mano[-4][0]==10 and self._color()) and not self._color()):
			return self._e()-self._real()-self._eColor()

	def escaleraColor(self):
		if(self._escalera() and self._color() and not (self.mano[0][0]==1 and self.mano[-4][0]==10 and self._color())):
			return self._eColor()

	def _nadaColor(self): # nada de color
		if(self._color()):
			return self._kolor()-self._eColor()-self._real()

	def _nada(self):
		if(not self._color()): # - nada de color - escaleras
			return self.cartas.diferentes(5, self.mano, algunasCartas = False)/self.cartas.jugadasPosibles*10000000-self._kolor()-self._e()

	def escaleraRC(self): #real de color
		if(self.mano[0][0]==1 and self.mano[-4][0]==10 and self._color()):
			return self._real()
		

juego = Baraja()

#-------------------------------------------------------------------------------------------------------

def transformation(x, y):
	return str(x).replace("11","J").replace("12","Q").replace("13","K").replace("1","A").replace("A0","10")+str(y)

n=int(input("Input: "))
print("\nOutput:\n")
if(n>10): n=0
for i in range(n):
    print("*****Jugada no.{0}*****".format(i+1))
    for j in juego.mano:
        print(transformation(j[0],j[1]), end=" ")
    print("")

    nada = True
    for f in Baraja.verification:
    	r = eval(compile('juego.'+str(f)+'()', '<string>', 'eval', __future__.division.compiler_flag))
    	try: 
    		print('Probabilidad:', str(int(r)/100000) +'%')
    		nada = False
    	except: pass
    if(nada):
    	for f in Baraja.els:
    		r = eval(compile('juego.'+str(f)+'()', '<string>', 'eval', __future__.division.compiler_flag))
    		try: print('Probabilidad:', str(int(r)/100000)+'%')
    		except: pass
    juego._actualizar()
print("*****Fin de emulacion*****")
