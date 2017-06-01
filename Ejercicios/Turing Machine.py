#turing machine
#d: derecha
#i: izquierda
#s: sin moverse
#v: vacio

def turing(cinta, ty):
	estado="a"
	posicion=0


	while True:
		tm=list(ty[estado,cinta[posicion]])
	
		estado=tm[0]

		new=list(cinta)
		new[posicion]=tm[1]
		cinta=''.join(new)

		if(tm[2]=="d"):
			posicion=posicion+1

		if(estado=="stop" or estado=="si" or estado=="no"):
			break

	return cinta


ty=dict()

ty["a","t"]=("a","t","d")
ty["a","0"]=("a","0","d")
ty["a","1"]=("a","1","d")
ty["a","v"]=("stop","0","s")

print(turing("t111vvvvv", ty))




