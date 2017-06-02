#Algoritmo de Euclides (divide y venceras)

#parametros
A=84
B=33

def euclides(a,b):
	print("A,B",a,b)
	if(a==b):
		return a
	elif(a>b):
		c=a//b
		r=a-c*b
		print("r,c",r,c)
		if(r==0):
			return b
		else:
			b=euclides(b,r)
		return b
	else:
		c=b//a
		r=b-c*a
		if(r==0):
			return a
		else:
			a=euclides(a,r)
		return a

print("MCD(A,B):", euclides(A,B))
