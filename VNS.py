#metaheuristica
import random
from random import choice
import string

#parametros
lineas=100
num_variables=50
variables=[]
for y in range(0,num_variables):
	variables.append("x"+str(y))

#Funcion que construye el problema 3satDNF
def conscnf(lineas, variables):
	f=open('cnfmeta.txt', 'w')
	for x in range(0,lineas):
		for y in range(0,3):
			k=choice([0,1])
			if(k==1):
				f.write("!")
			f.write(choice(variables))
			f.write("	")
		f.write("\n")
	f.closed

#funcion del 1er tipo de estructura de vecindario (cambia verdadero por falso y viceversa una sola variable)
def vec1(prueba_vec1):
	for i in range(0,num_variables):
		ccverdaderas=prueba_vec1.copy()
		bit="x"+str(i)
		if(bit in ccverdaderas):
			ccverdaderas.discard(bit)
		else:
			ccverdaderas.add(bit)
		if(eval(ccverdaderas)==True):
			return ccverdaderas
	return prueba_vec1

##funcion del 2do tipo de estructura de vecindario (2change)
def vec2(prueba_vec2):
	ccverdaderas=prueba_vec2.copy()
	for i in range(0,num_variables):
		bit1="x"+str(i)
		for y in range(i, num_variables):
			if(i==y):
				continue
			bit2="x"+str(y)
			if(bit1 in ccverdaderas and bit2 not in ccverdaderas):
				ccverdaderas.discard(bit1)
				ccverdaderas.add(bit2)
			elif(bit1 not in ccverdaderas and bit2 in ccverdaderas):
				ccverdaderas.add(bit1)
				ccverdaderas.discard(bit2)
			elif(bit1 in ccverdaderas and bit2 in ccverdaderas):
				ccverdaderas.discard(bit1)
				ccverdaderas.discard(bit2)
			else:
				ccverdaderas.add(bit1)
				ccverdaderas.add(bit2)
			if(eval(ccverdaderas)==True):
				return ccverdaderas
			ccverdaderas=prueba_vec2.copy()
	return prueba_vec2

#funcion del 3do tipo de estructura de vecindario (grupos de 3 consecutivos)
def vec3(prueba_vec3):
	lista=[]
	for i in range(0,3):
		lista.append(0)
	if (num_variables>2):
		for i in range(0,num_variables-3):
			ccverdaderas=prueba_vec3.copy()
			for y in range(0,3):
				lista[y]="x"+str(i+y)
				if(lista[y] in ccverdaderas):
					ccverdaderas.discard(lista[y])
				else:
					ccverdaderas.add(lista[y])
			if(eval(ccverdaderas)==True):
				return ccverdaderas
	return prueba_vec3

#busqueda de vec
def busqueda(pruebaf):
	pruebaf=vec1(pruebaf)
	if(eval(pruebaf)==False):
		pruebaf=vec2(pruebaf)
	else:
		return pruebaf
	if(eval(pruebaf)==False):
		pruebaf=vec3(pruebaf)
	else:
		return pruebaf
	return pruebaf

#funcion que realiza la parte constructiva del vns
def constrct(largo):
	g=open("cnfmeta.txt", "r")
	cont_v=[]
	cont_f=[]
	for i in range(0,num_variables):
		cont_v.append(0);
		cont_f.append(0);
	verdaderas=set()
	for linea in g:
		evaluacion=linea[:len(linea)-2].split("	")
		for y in range(0,len(evaluacion)):
			componente=evaluacion[y].split(",")
			if(componente[0][0]!="!"):
				cont_v[int(componente[0][1:])]+=1
			if(componente[0][0]=="!"):
				cont_f[int(componente[0][2:])]+=1
	for i in range(0,num_variables):
		cont_v[i]=cont_v[i]-cont_f[i];
	print("contt: ",cont_v)
	for i in range(0,int(num_variables/largo)):
		k=cont_v.index(max(cont_v))
		verdaderas.add("x"+str(k))
		cont_v[k]=-10000000
	g.close()
	return verdaderas

#funcion que escribe la instancia
def problema():
	f=open("cnfmeta.txt","r")
	print("\nproblema:")
	for linea in f:
		print(linea, end="")			



#Funcion que evalua los valores de asignacion a el problema y determina el resultado
def eval(prueba):
	l=open("cnfmeta.txt","r")

	resultado=False
	for linea in l:
		evaluacion=linea[:len(linea)-2].split("	")
		for y in range(0,len(evaluacion)):
			componente=evaluacion[y].split(",")
			if(componente[0][0]!="!"):
				hola=componente[0] in prueba
				if(hola==True):
					resultado=True
					break
			if(componente[0][0]=="!"):
				hola=componente[0][1:] in prueba
				if(hola==False):
					resultado=True
					break
			resultado=False
		if(resultado==False):
			return False
	return True

def escritura(solucionf):
	copysolucionf=solucionf.copy()
	l=open("solucionmeta.txt","w")
	while(len(copysolucionf)>0):
		k=copysolucionf.pop()
		l.write(str(k))
		l.write(" ")
	l.close()




#escritura 
conscnf(lineas, variables)

#escritura del problema
problema()

#construccion y busqueda de vec
conteo=1
while(1<=int(num_variables/conteo) and conteo<=10):
	verdaderas=constrct(conteo+1)
	asi=verdaderas
	print("verdaderas: ",verdaderas)
	if(eval(asi)==False):
		asi=busqueda(asi)
	else:
		break
	if(eval(asi)==True):
		break
	print("instancia (variables con valor verdadero): ",asi)
	conteo+=1

#evaluacion
print(" \nel resultado es ", eval(asi))

#escribir en txt
escritura(asi)