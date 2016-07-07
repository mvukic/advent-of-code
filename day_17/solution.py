import itertools

containers=[]
combinations=[]

with open("input.txt") as dataFile:
	for line in dataFile:
		size=int(line.rstrip())
		containers.append(size)
	containers.sort()

print(containers)

for i in range(1,len(containers)+1):
	comb = list(itertools.combinations(containers,i))
	print("Number of combinations for {} elements is {}".format(i,len(comb)))
	combinations.append(comb)
x=0
for comb in combinations:
	for tup in comb:
		if sum(tup) == 150:
			x+=1
			print("From combination of {} elements,tuple {} adds to 150.".format(len(tup),tup))

print("Combinations: {}".format(x))