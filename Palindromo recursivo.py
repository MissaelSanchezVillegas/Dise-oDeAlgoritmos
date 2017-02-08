#palrec

#funcion que checa si es paindromo la frase
def check(palindromo):
	if(len(palindromo)<=1):
		return True
	if(palindromo[0]==palindromo[len(palindromo)-1]):
		return check(palindromo[1:len(palindromo)-1])
	return False

#main
frase="holah"
if(check(frase)):
	print(frase," es palindromo")
else:
	print(frase," no es palindromo")