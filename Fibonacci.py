#fib

#funcion fibo
def fibo(ultimo,penultimo):
	result=ultimo+penultimo
	return result

#main
ultimo=1
penultimo=1
f=4
if(f<=2):
	ultimo=1
else:
	for x in range(1,f-1):
		aux=ultimo
		ultimo=fibo(ultimo,penultimo)
		penultimo=aux
print("valor de F6: ",ultimo)