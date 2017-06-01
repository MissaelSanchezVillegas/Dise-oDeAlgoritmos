#busqueda binaria
from random import randint

#parametros
tam=10
valor=randint(0,100)

#funcion que me crea 
def vector(tam):
	arreglo=list()
	for i in range(0,tam):
		if(len(arreglo)==0):
			arreglo.append(randint(0,100))
		else:
			k=randint(0,100)
			for y in arreglo:
				if(y>=k):
					indice=max(arreglo.index(y),0)
					arreglo.insert(indice,k)
					break
				if(y==arreglo[-1]):
					arreglo.append(k)
					break
	return arreglo

#funcion binaria
def binaria(arreglo,valor):
	if(len(arreglo)==0):
		return False
	k=arreglo[len(arreglo)//2]
	if(k==valor):
		return True
	elif(len(arreglo)==1):
		return False
	elif(valor>k):
		return binaria(arreglo[((len(arreglo)//2)+1):],valor)
	else:
		return binaria(arreglo[:(len(arreglo)//2)],valor)

arreglo=vector(tam)
resul=binaria(arreglo,valor)
print("arreglo: ",arreglo)
print("valor: ",valor)
if(resul==True):
	print("SI existe el valor en el arreglo")
else:
	print("NO existe el valor en el arreglo")
