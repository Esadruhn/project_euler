import math
import sys

def getNumber(n):
	if n == 0:
		return '(1/2)'
	else:
		return '(1/(2+'+getNumber(n-1)+'))'
		
if __name__ == "__main__":
	converg = int(sys.argv[1]);
	number = '1+'+getNumber(converg)
	
	
	
	print (number)
	