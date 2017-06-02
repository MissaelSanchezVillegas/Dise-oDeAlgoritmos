#metaheuristica
import random
from random import choice
import string

#parametros
lineas=50
num_variables=20
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
		evaluacion=eval(ccverdaderas)
		if(evaluacion[1]==1):
			return ccverdaderas
		if(evaluacion[0]>eval(prueba_vec1)[0]):
			prueba_vec1=ccverdaderas
			i=0
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
			evaluacion=eval(ccverdaderas)
			if(evaluacion[1]==1):
				return ccverdaderas
			if(evaluacion[0]>eval(prueba_vec2)[0]):
				prueba_vec2=ccverdaderas
				i=0
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
			evaluacion=eval(ccverdaderas)
			if(evaluacion[1]==1):
				return ccverdaderas
			if(evaluacion[0]>eval(prueba_vec3)[0]):
				prueba_vec3=ccverdaderas
				i=0
	return prueba_vec3

#busqueda de vec
def busqueda(pruebaf):
	i=0
	temp=eval(pruebaf)[0]
	while(i==0):
		pruebaf=vec1(pruebaf)
		evaluacion=eval(pruebaf)
		while(temp<evaluacion[0] and evaluacion[1]==0):
			temp=evaluacion[0]
			pruebaf=vec1(pruebaf)
			evaluacion=eval(pruebaf)
				
		if(evaluacion[1]==0):
			temp=evaluacion[0]
			pruebaf=vec2(pruebaf)
			evaluacion=eval(pruebaf)
			if(temp<evaluacion[0] and evaluacion[1]==0):
				continue

		else:
			return pruebaf
		if(evaluacion[1]==0):
			temp=evaluacion[0]
			pruebaf=vec3(pruebaf)
			evaluacion=eval(pruebaf)
			if(temp<evaluacion[0] and evaluacion[1]==0):
				continue
		else:
			return pruebaf
		i=1
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



#Funcion que evalua los valores de asignacion a el problema y determina el resultado en cantidad de clausulas cumplidas
def eval(prueba):
	l=open("cnfmeta.txt","r")

	resultado=[0,0]
	for linea in l:
		evaluacion=linea[:len(linea)-2].split("	")
		for y in range(0,len(evaluacion)):
			componente=evaluacion[y].split(",")
			if(componente[0][0]!="!"):
				hola=componente[0] in prueba
				if(hola==True):
					resultado[0]+=1
					resultado[1]=1
					break
			if(componente[0][0]=="!"):
				hola=componente[0][1:] in prueba
				if(hola==False):
					resultado[0]+=1
					resultado[1]=1
					break
			resultado[1]=0
		if(resultado[1]==0):
			return resultado
	return resultado

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
	if(eval(asi)[1]==0):
		asi=busqueda(asi)
	if(eval(asi)[1]==1):
		break
	print("instancia (variables con valor verdadero): ",asi)
	conteo+=1

#evaluacion
evaluacion=eval(asi)
if(evaluacion[1]==0):
	res=False
else:
	res=True
print(" \nel resultado es ", evaluacion[0], "CLAUSULAS VERDADERAS \n", "Con resultado final", res, "solucion: ", asi)

#escribir en txt
escritura(asi)
