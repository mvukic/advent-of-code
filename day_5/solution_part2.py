number_of_nice_strings=0

with open("input.txt") as input:
	for line in input:
		line=line.rstrip()
		cond1=False
		for index,char in enumerate(line):
			if index+2 == len(line):
				break
			if char == line[index+2]:
				cond1=True
				break
		cond2 = False
		index = 0
		while True:
			if index+1 == len(line):
				break
			if line[index:index+2] in line[index+2:]:
				# print("{} has {}".format(line,line[index:index+2]))
				cond2 = True
				break
			index +=1			
		if cond1 and cond2:
			number_of_nice_strings += 1

print("Number of good strings is : {}".format(number_of_nice_strings))