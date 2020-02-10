import math

def sumOfMultiples (high):
	sum = 0;
	for n in range(0, math.floor(high/3)+1):
		if n*3 < high:
			sum = sum + n*3
		if n*5 < high and n*5 % 3 != 0:
			sum = sum + n*5
	return sum

if __name__ == "__main__" :
	print (sumOfMultiples(1000))
	