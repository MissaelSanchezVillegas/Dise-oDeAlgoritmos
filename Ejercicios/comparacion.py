#comparacion

n=2
pol=n**10
exp=1.001**n
while (pol>exp):
	n=n*2
	pol=n**10
	exp=1.001**n
print(n/2)
n=n/2
pol=n**10
exp=1.001**n
while (pol>exp):
	n=n+1
	pol=n**10
	exp=1.001**n
print(n-1)