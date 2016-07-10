from pprint import pprint


matrix={}

with open("input.txt",'r') as dataFile:
	for index,line in enumerate(dataFile):
		line=list(line.rstrip())
		for i in range(0,len(line)):
			matrix[index,i]= line[i]

pprint(matrix)
		