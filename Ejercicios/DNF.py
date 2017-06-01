import random
from random import choice
import string

#parametros
lineas=20
num_variables=10
variables=[]
for y in range(0,num_variables):
	variables.append("x"+str(y))

#Funcion que construye el problema 3satDNF
def conscnf(lineas, variables):
	f=open('dnf.txt', 'w')
	for x in range(0,lineas):
		linea=random.sample(variables, 3)
		for y in range(0,3):
			k=choice([0,1])
			if(k==1):
				f.write("!")
			f.write(linea[y])
			f.write("	")
		f.write("\n")
	f.closed

#Funcion asigna los valores de las variables (TRUE or FALSE)
def asignacion(variables,num_variables):
	f=open("asi.txt", "w")
	for x in range(0,num_variables):
		y=choice((0,1))
		if(y==1):
			f.write(variables[x])
			f.write(" ")
	f.closed

#Funcion que evalua los valores de asignacion a el problema y determina el resultado
def eval():
	l=open("dnf.txt","r")
	print(" \nproblema:")
	resultado=False
	for linea in l:
		evaluacion=linea[:len(linea)-2].split("	")
		print(evaluacion)
		for y in range(0,len(evaluacion)):
			componente=evaluacion[y].split(",")
			if(componente[0][0]!="!"):
				hola=componente[0] in asi
				if(hola==False):
					break
			if(componente[0][0]=="!"):
				hola=componente[0][1:] in asi
				if(hola==True):
					break
			if(y==len(evaluacion)-1):
				resultado=True
		if(resultado==True):
			return resultado
	return resultado



#escritura 
conscnf(lineas, variables)
asignacion(variables,num_variables)

#lectura de asignacion
f=open("asi.txt","r")
asi=f.readline()
asi=set(asi[:len(asi)-1].split(" "))
print("instancia (variables con valor verdadero): ",asi)
f.closed

#evaluacion
print(" \nel resultado es ", eval())