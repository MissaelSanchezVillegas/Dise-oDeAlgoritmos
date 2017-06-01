#binomio
import math
def binom(n,k,exact):
	y=1
	if(exact==True):
		if(k<(n-k)):
			for x in range(n-k+1,n+1):
				y=x*y
			result=y/(math.factorial(k))
		else:
			for x in range(k,n+1):
				y=x*y
				print(y)
			result=y/(math.factorial(n-k))
	else:
		y=0
		if(k<(n-k)):
			for x in range(n-k+1,n+1):
				y=y+math.log(x)
			for x in range(1,k+1):
				y=y-math.log(x)
			result=y
		else:
			for x in range(k,n+1):
				y=y+mat.log(x)
			for x in range(1,n-k+1):
				y=y-mat.log(x)
			result=y
		result=math.exp(result)
	return result


#main
print (binom(20,8,False))
