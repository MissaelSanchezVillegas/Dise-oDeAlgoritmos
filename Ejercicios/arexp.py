#arbol de expansion

def reach():
	f = open("arexp.txt","r");
	niveles=dict()
	costo=0
	for i in f:
		x,y,c=(i.strip()).split()
		w=niveles.get(x,{x}) | niveles.get(y,{y})
		for l in w:
			niveles[l]=w
		print(niveles)
	return False

if(reach()==True):
	print("si hay camino")
else:
	print("no lo hay")