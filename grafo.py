#grafos
from random import choice


#funcion que verifica todos los vecinos conectados
def vecinos(nodo,arista,listanodos):
	vec=set()
	for x in range(0,len(listanodos)):
		if(arista[nodo][x].existe==True):
			vec.add(listanodos[x])
	return vec

#datos de la arista
class caristas:
	def __init__(self,origen,destino,peso,existe):
		self.existe=existe
		self.peso=peso
		self.origen=origen
		self.destino=destino
	def __str__(self):
		return str(self.peso)
	peso=0

#datos de el nodo
class nodos:
	def __init__(self, numero, demanda, produccion):
		self.id=int(numero)
		self.demanda=demanda
		self.produccion=produccion
	def __str__(self):
		return str(self.id)


#creacion y parametro de los nodos
f = open("inst.txt","r");
lines = f.readlines();
numnodo=lines[0].split(" ")
listanodos=[]
k=-1
for i in lines:
	k=k+1
	linea=lines[k].split(" ")
	if(linea[0]=="c"):
		listanodos.append(nodos(linea[1],linea[2],0))
	if(linea[0]=="f"):
		listanodos.append(nodos(linea[1],0,linea[2]))
	

#creacion de las aristas dependiendo de cada nodo
arista = {}
for i in range(n):
	arista[i]={}
	for j in range(n):
		arista[i][j]=caristas(listanodos[i].id,listanodos[j].id,0,False)

#parametros de las aristas
k=0
for i in lines:
	k=k+1
	if(k>n+1):
		thisline=i.split(" ")
		arista[int(thisline[1])][int(thisline[2])].peso=int(thisline[3])
		print("arista", int(thisline[1]), int(thisline[2]),  arista[int(thisline[1])][int(thisline[2])].peso)
		arista[int(thisline[1])][int(thisline[2])].existe=True
f.close()
#conjunto de elementos marcados
marcados=set()

#pila
pila=[]

#DFS
nodo_inicial=listanodos[0]
marcados.add(nodo_inicial)
pila.append(nodo_inicial)
while(len(pila)>0):
	veci=vecinos(pila[-1].id,arista,listanodos)
	veci=list(veci-marcados)
	verif=list(pila)
	print(verif[-1].id)
	if(len(veci)>0):
		visitado=choice(veci)
		marcados.add(visitado)
		pila.append(visitado)
	else:
		pila.pop()
		






