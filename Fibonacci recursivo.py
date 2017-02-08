#fibonacci rec

#funcion fibo
def fibo(n):
	if(n<2):
		return n
	return(fibo(n-1)+fibo(n-2))

#main
valor=1
n=15
print("hola")
if(n>2):
	valor=fibo(n)
print("valor de F6: ",valor)