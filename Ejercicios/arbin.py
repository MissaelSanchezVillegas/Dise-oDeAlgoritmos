#arboles binarios
from random import randint

class nodo:
	def __init__(self,valor):
		self.valor=valor
		self.izq=None
		self.der=None

	def add(self, new):
		if(new>self.valor):
			if(self.der==None):
				self.der=nodo(new)
			else:
				return self.der.add(new)
			return True
		elif(new<self.valor):
			if(self.izq==None):
				self.izq=nodo(new)
			else:
				return self.izq.add(new)
			return True
		else:
			return False

	def consultar(self,numero):
		if(numero==self.valor):
			print("existe")
			return True
		elif(numero>self.valor):
			if(self.der==None):
				print("no existe")
				return False
			else:
				self.der.consultar(numero)
		else:
			if(self.izq==None):
				print("no existe")
				return False
			else:
				self.izq.consultar(numero)

	def borrar(self,numero):
		if(numero>self.valor):
			if(self.der==None):
				print("no existe")
				return False
			else:
				self.der.borrar(numero)
		else:
			if(self.izq==None):
				print("no existe")
				return False
			else:
				self.izq.borrar(numero)	


	def __str__(self):
		v=""
		if(self.izq!=None):
			v+=self.izq.__str__()
		v+= str(self.valor)+" "
		if(self.der!=None):
			v+=self.der.__str__()
		return v


def imprimir(raiz):
	if(raiz.izq!=None):
		imprimir(raiz.izq)
	print(raiz.valor)
	if(raiz.der!=None):
		imprimir(raiz.der)



raiz=nodo(10)
for i in range(0,10):
	raiz.add(randint(2,50))

imprimir(raiz)
print(raiz)
raiz.consultar(6)




