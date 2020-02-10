

def checkIfLeap(year) :
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def getNbDaysInMonth(month, year) :
	if month == 0:
		return 31;
	elif month == 1:
		if checkIfLeap(year):
			return 29;
		else:
			return 28;
	elif month == 2:
		return 31;
	elif month == 3:
		return 30;
	elif month == 4:
		return 31;
	elif month == 5:
		return 30;
	elif month == 6:
		return 31;
	elif month == 7:
		return 31;
	elif month == 8:
		return 30;
	elif month == 9:
		return 31;
	elif month == 10:
		return 30;
	elif month == 11:
		return 31;
		
if __name__ == "__main__":

	startingDay = 365 % 7;
	sum = 0;
	
	if startingDay == 6:
					sum += 1
					
	for year in range(1901, 2001):
		for month in range(0, 12):
			if month == 12 and year == 2001:
				startingDay = 0
			else:
				startingDay = (getNbDaysInMonth(month, year) + startingDay) % 7	
			if startingDay == 6:
					sum += 1
	print (sum)