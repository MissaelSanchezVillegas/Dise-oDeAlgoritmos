#dinamico
from random import choice
costo=0
secval=20
maxval=20
umbralmax=maxval*(3/4)
umbralmin=maxval*(1/4)
taminicial=8

def func(secuencia,maxval,umbralmax,umbralmin,taminicial):
	global costo
	valor=taminicial
	valorinicial=maxval
	for x in secuencia:
		if(x==1):
			valor+=1
			if(valor>umbralmax):
				costo+=valor
				maxval=maxval*2
		if(x==0):
			if(valor>0):
				valor-=1
				if(valor<umbralmin and valor>taminicial):
					costo+=valor
					maxval=maxval//2
		umbralmax=maxval*(3/4)
		umbralmin=maxval*(1/4)
	return costo

secuencia=list()
for x in range(0,secval):
	secuencia.append(choice([1,0]))
print(secuencia)
print("costo: ",func(secuencia,maxval,umbralmax,umbralmin,taminicial))


