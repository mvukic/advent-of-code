
floor=0

with open("input.txt") as dataFile:
	line = dataFile.readline().rstrip()
	for index,direction in enumerate(line):
		if direction == "(":
			floor +=1
		else:
			floor -=1
		if floor == -1:
			print("Basement index is : {}".format(index+1))
			break
