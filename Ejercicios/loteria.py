from random import choice
import sys
loteria_numeros=[]
loteria=["gallo","diablito", "dama","catrin","paraguas","sirena","escalera","botella","barril","arbol","melon","valiente","gorrito","muerte","pera","bandera","bandolon","violoncello","garza","pajaro","mano","bota","luna","cotorro","borracho","negrito","corazon","sandia","tambor","camaron","jaras","musico","araña","soldado","estrella","cazo","mundo","apache","nopal","alacran","rosa","calavera","campana","cantarito","venado","sol","corona","chalupa","pino","pescado","palma","maceta","arpa","rana"]
for x in range(0,54):
	y=x
	loteria_numeros.append(y)
	print (loteria_numeros[x])
	print (loteria[x])

while (len(loteria_numeros)>0):
	sel=choice(loteria_numeros)
	print("\n")
	print(loteria[sel])
	print(len(loteria_numeros))
	input()
	loteria_numeros.remove(sel)
