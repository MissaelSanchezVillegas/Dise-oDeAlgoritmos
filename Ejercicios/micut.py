#Actividad hecha por Missael Sánchez Villegas y José Anastacio Hernández Saldaña
from random import shuffle
grafo = [(1, 3), (2, 3), (2, 4), (3, 4), (4, 6), (5, 6)]
from copy import deepcopy
cand = deepcopy(grafo)
shuffle(cand) #aleatorizacion de aristas
comp = dict() #componentes
for (u, v) in grafo:   #crea las componentes iniciales para todo nodo
    comp[u] = {u}
    comp[v] = {v}
n = len(comp.keys())   #cantidad de componentes
menor = min(comp.keys())
while len(cand) > 0:     #hacerlo mientras halla aristas
    (u, v) = cand.pop()   #seleccionar la arista
    c = comp[v]          #c es la componente de v
    if u not in c:       #si u no esta en la componente c unes las componentes en una nueva
        nuevo = c.union(comp[u])
        for w in nuevo:
            comp[w] = nuevo  #creamos la nueva componente
        n -= 1
        if n == 2:
            break       #paramos cuando halla 2 componentes
corte = 0
for arista in grafo:    #contamos el valor del corte
    (u, v) = arista
    if comp[u] != comp[v]:
        corte += 1
print(comp[menor])
for v in comp:          #impriimimos los conjuntos
    if menor not in comp[v]:
        print(comp[v])
        break
print(corte)
