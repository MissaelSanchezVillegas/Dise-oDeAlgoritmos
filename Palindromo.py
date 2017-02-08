#pal
import sys

#funcion que checa si las letras en los indices son iguales
def check(primero, ultimo):
	if(primero==ultimo):
		return True
	else:
		return False

#main
frase="hooh"
i1=0
i2=len(frase)-1

while (i1<i2):
	if(check(frase[i1],frase[i2])==False):
		print(frase," no es un palindromo")
		sys.exit(0)
	i1=i1+1
	i2=i2-1

print(frase," es palindromo")