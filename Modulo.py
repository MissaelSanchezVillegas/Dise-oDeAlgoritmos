#modulo
import math
def verpar(exp):
	if(exp%2==0):
		return True
	else:
		return False
def modu(exp,v,y,r):
	par=verpar(exp)
	while(exp>0):
		par=verpar(exp)
		if(par==False):
			r=r*v
			r=r%y
		v=v*v
		v=v%y
		exp=exp>>1

	return r
def exponente(exp,v,y):
	resultado=(math.pow(v,exp))
	resultado=resultado%y
	return resultado

print("El valor final del modulo bajo el metodo del modulo es:",modu(2,23,24,1))
print("El valor final del modulo bajo el metodo del pow es:",exponente(2,23,24))