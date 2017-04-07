#quicksort
from random import random
costo=0
def qs(array):
	global costo
	if(len(array)==2):
		costo += 1
		return sorted(array)
	if(len(array)<2):
		return array
	mayores=list()
	menores=list()
	pivote=array.pop(len(array)-1)

	for x in array:
		if(x<pivote):
			costo +=1
			menores.append(x)
		else:
			costo+=1
			mayores.append(x)
	return qs(menores)+[pivote]+qs(mayores)

def gen(largo):
	array=list()
	for i in range(0,largo):
		array.append(random())
	return array


f=open("quicksort.txt","w")
y=1
prom=0
while(y<10000):
	for x in range(0,10):
		qs(gen(y))
		print(y,costo)
		prom+=costo
		costo=0
	prom=prom/10
	f.write(str(y))
	f.write(" ")
	f.write(str(prom))
	f.write("\n")
	prom=0
	y=y*2








