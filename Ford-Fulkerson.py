#generadora de instancia
from random import randint
from random import normalvariate
from random import choice

#funcion que escribe un espacio
def esp(f):
	f.write(" ")

def graforesidual(grafo):
	res=dict()
	for c,d in grafo.keys():
		res[(d,c)]=0
	return res

def capresidual(grafo,camino):
	minimo=10000000
	for i in camino:
		if(minimo>grafo[(i)]):
			minimo=grafo[(i)]
	return minimo
		
def caminodict(aristas,inicial, final):
	lista=camino(aristas,inicial, final)
	if(lista==False):
		return False
	nlista=list()
	for i in range(0,len(lista)-1):
		nlista.append((lista[i],lista[i+1]))
	return nlista

def camino(aristas,inicial, final):
	vec=set()
	marcados=set()
	pila=[]
	nodo_inicial=inicial
	marcados.add(nodo_inicial)
	pila.append(nodo_inicial)
	while(len(pila)>0):
		veci=vecinos(aristas,pila[-1])
		#print("vecinos: ",veci)
		veci=list(veci-marcados)
		verif=list(pila)
		#print(verif[-1])
		if(len(veci)>0):
			visitado=choice(veci)
			marcados.add(visitado)
			pila.append(visitado)
			if(visitado==final):
				return pila
		else:
			pila.pop()
	return False
	
def bfs(inicial, aristas):
	marcados=set()
	pila=[]
	nodo_inicial=inicial
	niveles=dict()
	ultimo_nivel=set()
	ultimo_nivel.add(nodo_inicial)
	otros=set()
	niveles[nodo_inicial]=0
	y=1

	while(len(ultimo_nivel)>0):
		for x in ultimo_nivel:
			unir=vecinos(aristas,x)
			otros=otros.union(unir)
		ultimo_nivel.clear()
		for x in otros:
			if x not in niveles:
				niveles[x]=y
				ultimo_nivel.add(x)
		y=y+1

	return marcados

def dfs(inicial, aristas):
	marcados=set()
	pila=[]
	nodo_inicial=inicial
	marcados.add(nodo_inicial)
	pila.append(nodo_inicial)
	while(len(pila)>0):
		veci=vecinos(aristas,pila[-1])
		print("vecinos: ",veci)
		veci=list(veci-marcados)
		verif=list(pila)
		print(verif[-1])
		if(len(veci)>0):
			visitado=choice(veci)
			marcados.add(visitado)
			pila.append(visitado)
		else:
			pila.pop()
	return marcados

#funcion que arroja los vecinos de un nodo (ya sea que van a el o que vienen de el)
def vecinosff(aristas,nodo):
	vec=set()
	for (c,d) in aristas.keys():
		if c==nodo:
			vec.add(d)
		elif d==nodo:
			vec.add(c)
		else:
			continue
	return vec

def vecinos(aristas, nodo):
	vec=set()
	for (c,d) in aristas.keys():
		if c==nodo:
			vec.add(d)
		else:
			continue
	return vec

#funcion que crea el grafo
def graf(nodos,media,var,inicio,fin):
	if(fin>=nodos or fin<nodos-1):
		print("error en el parametro del nodo final")
		return 0
	valor=randint(2,5)
	aristas=randint(nodos-1,int((nodos-1)+(nodos*(nodos-1)/2-(nodos-1))/valor))
	print("aristas: ", aristas)
	if (aristas>nodos*(nodos-1)/2):
		print("es un mutligrafo")
		return 0
	n=dict()
	s=0
	t=randint(1,nodos-1)
	n[(s,t)]=int(normalvariate(media,var))
	arbol=set()
	arbol.add(s)
	arbol.add(t)
	listanodos=[]
	for i in range(0,nodos):
		listanodos.append(i)
	for i in listanodos:
		if len(vecinosff(n,i))==0:
			nuevo=arbol.pop()
			n[(nuevo,i)]=int(normalvariate(media,var))
			arbol.add(nuevo)
			arbol.add(i)
	#print("antes: ", n)
	if(aristas-nodos+1<0):
		print("grafo disconexo")
		return 0
	else:
		for i in range(0,aristas-nodos+1):
			inicial=randint(0,nodos-2)
			final=inicial
			j=1
			while final==inicial or final in vecinosff(n,inicial):
				if(j>25):
					break
				final=randint(1,nodos-1)
				j+=1
			if(j>25):
				continue
			n[(inicial,final)]=int(normalvariate(media,var))
	res=graforesidual(n)

	print("grafo: ", n)
	#algoritmo ford fulkerson
	path=caminodict(n,inicio,fin)
	temp=list()
	flujo=0
	while (path!=False):
		minimo=capresidual(n,path)
		flujo+=minimo
		print("flujo: ",flujo)
		for c,d in n.keys():
			if((c,d) in path):
				n[(c,d)]=n[(c,d)]-minimo
				res[(d,c)]=res[(d,c)]+minimo
			if(n[(c,d)]==0):
				temp.append((c,d))
		for i in range(0,len(temp)):
			del(n[temp[i]])
		temp.clear()
		path=caminodict(n,inicio,fin)

	#resultado de flujo y grafo de flujo
	grafoflujo=dict()
	for c,d in res.keys():
		if(res[(c,d)]>0):
			grafoflujo[(d,c)]=res[(c,d)]
	print("grafo despues de Ford-Fulk: ",n)
	print("\ngrafo del flujo:", grafoflujo)
	print("flujo:", flujo)

graf(100,25,5,0,99)