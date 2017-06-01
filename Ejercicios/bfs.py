#BFS
from random import randint

#funcion que escribe un espacio
def esp(f):
	f.write(" ")

#funcion que crea los nodos y aristas del problema(instancia)
def graf(nodos_cliente,nodos_fabrica):
	#demanda y capacidad de produccion de nodos clientes y fabricas respectivamente
	dem_clientes=[]
	cap_fabrica=[]
	demanda=0
	capacidad=0
	for x in range(0,nodos_cliente):
		dem_clientes.append(randint(5, 100))
		demanda=dem_clientes[x]+demanda
	for x in range(0,nodos_fabrica):
		cap_fabrica.append(randint(5,100))
		capacidad=capacidad+cap_fabrica[x]
	while(demanda>capacidad):
		cap_fabrica[randint(0,nodos_fabrica-1)]+=int(demanda/10)
		capacidad+=int(demanda/10)


	f = open("inst.txt","w");
	#cracion del renglon de datos del grafo
	f.write("g "), f.write(str(nodos_cliente+nodos_fabrica)), esp(f), f.write(str(nodos_cliente*nodos_fabrica)), f.write("		#numero_de_nodos,numero_de_aristas"), f.write("\n")
	
	#nodos
	for x in range(0,nodos_cliente):
		f.write("c "), f.write(str(x)), esp(f), f.write(str(dem_clientes[x])), esp(f), f.write("         #parametros del nodo cliente: etiqueta, demanda"), f.write("\n")
	for x in range(0,nodos_fabrica):
		f.write("f "), f.write(str(x+nodos_cliente)), esp(f), f.write(str(cap_fabrica[x])), esp(f), f.write("         #parametros del nodo fabrica: etiqueta, produccion"), f.write("\n")
	
	#aristas
	for x in range(0,nodos_cliente):
		for y in range(nodos_cliente,nodos_fabrica+nodos_cliente):
			f.write("a "), f.write(str(x)), esp(f), f.write(str(y)), esp(f), f.write(str(randint(2,20))), f.write(" 	#parametros de la arista: nodo inicial, nodo final, costo \n")
			f.write("a "), f.write(str(y)), esp(f), f.write(str(x)), esp(f), f.write(str(randint(2,20))), f.write(" 	#parametros de la arista: nodo inicial, nodo final, costo \n")

	f.close()

graf(10,12)





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
n=int(numnodo[1])
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

#BFS
nodo_inicial=listanodos[0]
niveles=dict()
ultimo_nivel=set()
ultimo_nivel.add(nodo_inicial.id)
otros=set()
niveles[nodo_inicial.id]=0
y=1

while(len(ultimo_nivel)>0):
	for x in ultimo_nivel:
		unir=vecinos(x,arista,listanodos)
		otros=otros.union(unir)
	ultimo_nivel.clear()
	for x in otros:
		if x.id not in niveles:
			niveles[x.id]=y
			ultimo_nivel.add(x.id)
	y=y+1

print(niveles)

