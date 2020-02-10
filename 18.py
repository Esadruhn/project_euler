import sys
	
if __name__ == "__main__":
	# p067_triangle.txt
	# 18file.txt
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()
		lastLine = []
		currentLine = []
		
		for i in range(len(lines)-1, -1, -1):
		
			numbers = [int(x) for x in lines[i].split(' ')]
			
			if(len(lastLine) == 0):	
				currentLine = numbers
			else:
				for index, number in enumerate(numbers):
					currentLine.append(number + max(lastLine[index], lastLine[index+1]))
			
			lastLine = currentLine;
			currentLine = []
			
		print(lastLine[0])
				
				
			