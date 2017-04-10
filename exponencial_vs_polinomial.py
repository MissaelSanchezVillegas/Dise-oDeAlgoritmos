#exponencial vs polinomial
def func():
	f=open("exp.txt","w")
	x=2
	exp=1.1**x
	pol=x**70
	while(exp<=pol):
		f.write(str(x) + " " + str(exp) + " " + str(pol) + "\n")
		x=x+1
		exp=1.1**x
		pol=x**70
	f.close
	return x
valor=func()
print("valor: ", valor)