#mochila transicion de fase

from random import randint
from random import choice
import collections

def creacion(items, capacidad, inferiorvalor, superiorvalor, inferiorcap, superiorcap):
	f = open("tdf.txt","w")
	f.write(str(capacidad))
	f.write(" capacidad\n")
	for x in range(0,items):
		f.write(str(randint(inferiorvalor,superiorvalor)) +" "+ str(randint(inferiorcap,superiorcap)))
		f.write(" valor y capacidad del item "+str(x))
		f.write("\n")
	f.closed

def lectura():
	f=open("tdf.txt","r")
	lines = f.readlines()
	diccionario=dict()
	k=0
	for x in lines:
		if k>0:
			datos=x.split(" ")
			diccionario[k]=(int(datos[0]),int(datos[1]))
		k+=1
	return diccionario

def ratio(dicc):
	newd=dict()
	for a,(b,c) in dicc.items():
		newd[b/c]=a
	ordenado=collections.OrderedDict(sorted(newd.items(), reverse=True))
	ordenado=dict(ordenado)
	return ordenado

def ben(dicc,sol):
	beneficio=0
	for a,(b,c) in dicc.items():
		if a in sol:
			beneficio+=b
	return beneficio


#creacion de la instancia
capacidad=100
creacion(20,capacidad,2,10,10,30)
alpha=0.5

#lectura inst
diccionario=lectura()
print("instancia \"item:(valor,capacidad)\"\n",diccionario)
ordenado=ratio(diccionario)
LRC=dict()
solucion=list()
capsol=0


#construccion greedy aleatorizado
while(True):
	bol=True
	k=0
	for rat,item in ordenado.items():
		if(k>len(ordenado)*alpha and len(ordenado)>5):
			break
		LRC[item]=rat
		k=k+1
	if(len(LRC)==0):
		break
	while(len(LRC)>0 and bol):
		ladrillo=choice(list(LRC.items()))
		if(capsol+diccionario[ladrillo[0]][1]<=capacidad):
			capsol+=diccionario[ladrillo[0]][1]
			solucion.append(ladrillo[0])
			del(ordenado[ladrillo[1]])
			bol=False
		else:
			del(LRC[ladrillo[0]])
	if(len(LRC)==0):
		break
	LRC.clear()


print("\nsolucion", solucion)
print("capacidad de la solucion: ",capsol)
print("beneficio: ", ben(diccionario,solucion))
	











