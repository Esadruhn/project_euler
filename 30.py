import math
import functools

if __name__ == "__main__": 	
	sum = 0;
	print ('test reduce ' + str(functools.reduce(lambda x,y: x+y, [1,2,3], 0)))
	for i in range(2, 10**7):
		k = 0
		number = i
		decomp=[]
		for k in range(6,-1,-1):
			if(i >= 10**k):
				ak = math.floor(number/10**k)
				decomp.append(ak)
				number -= ak*10**k
		if i == functools.reduce(lambda x,y: x+y, map(lambda x:x**5, decomp), 0):
			sum += i
			print(str(i) + ' ' + str(decomp))
	print (sum)