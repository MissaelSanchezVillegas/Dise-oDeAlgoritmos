#grafos

class aristas:
	def __init__(self):
		self.peso ={}
	def __str__(self):
		return str(self.peso)
class nodos:
	def __init__(self, numero):
		self.id=numero
	def __str__(self):
		return str(self.id)

n=20
listanodos=[]
for i in range(n):
	listanodos.append(nodos(i+1))
	print(listanodos[i])

ar = []
for i in range(n):
    ar.append([])
    for j in range(n):
        ar[i].append(1)
