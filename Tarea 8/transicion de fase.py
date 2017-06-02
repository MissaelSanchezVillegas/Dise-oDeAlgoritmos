#transiciones de fase

from random import randint
from random import choice
import collections
import time

#parametros
itercap=800 #cuantas iteraciones en capacidades en multiplos de 10
numobjetos=100 #numero de objetos
inferiorvalor=2 #limite inferior de valor
superiorvalor=10 #limite superior de valor
inferiorcap=10 #limite inferior de peso
superiorcap=30 #limite superior de cap
alpha=0.5 #parametro para la lista restringida de candidatos

def creacion(items, inferiorvalor, superiorvalor, inferiorcap, superiorcap):
	f = open("tdf.txt","w")
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
	f.closed
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

def busqueda(solucion,beneficio,capsol,capm,dicc):
	valort=beneficio
	capacidadt=capsol
	bol=True
	k=0
	cand=list()
	while(bol):
		mej=False
		cand.clear()
		for a,(b,c) in dicc.items():
			if a not in solucion:
				cand.append(a)
		for j in cand:
			for i in solucion:
				if(dicc[j][1]+capacidadt-dicc[i][1]<=capm):
					temp=solucion.copy()
					temp.remove(i)
					temp.append(j)
					valornuevo=ben(dicc,temp)
					if(valornuevo>valort):
						mej=True
						temp2=temp.copy()
						capnueva=dicc[j][1]+capacidadt-dicc[i][1]
						break
					temp.clear()	
			if(mej==True):
				solucion=temp2.copy()
				capacidadt=capnueva
				valort=valornuevo
				break
			else:
				bol=False
				break
		if(len(cand)==0):
			bol=False
	return solucion,capacidadt,valort

def datosgrafica(lista):
	f=open("datosgrafica.txt","w")
	f.write("capacidad en mochila,tiempo(segundos) \n")
	for (a,b) in lista:
		f.write(str(a)+",")
		f.write(str(b))
		f.write(" \n")
	f.closed


resultado=list()
creacion(numobjetos,inferiorvalor,superiorvalor,inferiorcap,superiorcap)

for z in range(1,itercap):
	t0=time.clock()
	#creacion de la instancia
	capacidad=10*z

	#lectura inst
	diccionario=lectura()
	#print("instancia \"item:(valor,capacidad)\"\n",diccionario)
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

	#busqueda local

	beneficio=ben(diccionario,solucion)
	#print("\nsolucion", solucion)
	#print("capacidad de la solucion: ",capsol)
	#print("beneficio: ", beneficio)

	(nuevasolucion,capsol,beneficio)=busqueda(solucion,beneficio,capsol,capacidad,diccionario)
	#print("\n nuevasolucion: ", nuevasolucion)
	#print("capacidad de la solucion: ",capsol)
	#print("beneficio: ", beneficio)

	tf=time.clock()
	print("segundos: ",tf-t0)

	resultado.append((capacidad,tf-t0))

print(resultado)
datosgrafica(resultado)