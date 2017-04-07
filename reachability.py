#reach

#creacion y parametro de los nodos
def reach():
	f = open("reach.txt","r");
	niveles=dict()
	header = f.readline()
	inicio=header.split(" ")[0]
	fin=header.split(" ")[1]
	for i in f:
		x,y=(i.strip()).split()
		w=niveles.get(x,{x}) | niveles.get(y,{y})
		if(inicio in w and fin in w):
			return True
		for l in w:
			niveles[l]=w
	print(niveles)
	return False

#verifica si hay camino o no
if(reach()==True):
	print("si hay camino")
else:
	print("no lo hay")



