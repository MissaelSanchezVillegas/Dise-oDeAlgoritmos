#generadora de instancia
from random import randint

#funcion que escribe un espacio
def esp(f):
	f.write(" ")

#funcion que crea los nodos y aristas del problema
def graf(nodos_cliente,nodos_fabrica):
	#demanda y capacidad de produccion de nodos clientes y fabricas respectivamente
	dem_clientes=[]
	cap_fabrica=[]
	demanda=0
	capacidad=0
	for x in range(0,nodos_cliente):
		dem_clientes.append(randint(5, 100))
		demanda=dem_clientes[x]+demanda
	for x in range(0,nodos_fabrica):
		cap_fabrica.append(randint(5,100))
		capacidad=capacidad+cap_fabrica[x]
	while(demanda>capacidad):
		cap_fabrica[randint(0,nodos_fabrica-1)]+=int(demanda/10)
		capacidad+=int(demanda/10)


	f = open("inst.txt","w");
	#cracion del renglon de datos del grafo
	f.write("g "), f.write(str(nodos_cliente+nodos_fabrica)), esp(f), f.write(str(nodos_cliente*nodos_fabrica)), f.write("		#numero_de_nodos,numero_de_aristas"), f.write("\n")
	
	#nodos
	for x in range(0,nodos_cliente):
		f.write("c "), f.write(str(x)), esp(f), f.write(str(dem_clientes[x])), esp(f), f.write("         #parametros del nodo cliente: etiqueta, demanda"), f.write("\n")
	for x in range(0,nodos_fabrica):
		f.write("f "), f.write(str(x+nodos_cliente)), esp(f), f.write(str(cap_fabrica[x])), esp(f), f.write("         #parametros del nodo fabrica: etiqueta, produccion"), f.write("\n")
	
	#aristas
	for x in range(0,nodos_cliente):
		for y in range(nodos_cliente,nodos_fabrica+nodos_cliente):
			f.write("a "), f.write(str(x)), esp(f), f.write(str(y)), esp(f), f.write(str(randint(2,20))), f.write(" 	#parametros de la arista: nodo inicial, nodo final, costo \n")
			f.write("a "), f.write(str(y)), esp(f), f.write(str(x)), esp(f), f.write(str(randint(2,20))), f.write(" 	#parametros de la arista: nodo inicial, nodo final, costo \n")

	f.close()

graf(10,12)
