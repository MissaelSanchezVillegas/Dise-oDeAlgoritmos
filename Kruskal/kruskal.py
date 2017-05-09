#Actividad hecha por Missael Sánchez Villegas y José Anastacio Hernández Saldaña
import graph
import InstanciesGenerator

dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 10, 2)
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.normal, 2, 5)
generador = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.connected,distribution_weight = dw,distribution_degree = dd, directed = False )
g = generador.generateInstance('Test', 10, 50)

#lv = {}
#for x in g.vertices:
#   print(x, g.closenesscentrality(x))

print(g)
k = g.kruskal()

for r in range(10):
	dfs =  k.deepfirstsearch()
	c = 0
	for f in range(len(dfs) -1):
		c += g[dfs[f]].neighbors[dfs[f+1]]
		print(dfs[f], dfs[f+1], g[dfs[f]].neighbors[dfs[f+1]] )

	c += g[dfs[-1]].neighbors[dfs[0]]
	print(dfs[-1], dfs[0], g[dfs[-1]].neighbors[dfs[0]])
	print('costo',c)



