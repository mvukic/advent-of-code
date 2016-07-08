from pprint import pprint
import itertools

def Main():
	people={}
	names=[]
	with open("input.txt","r") as dataFile:
		for line in dataFile:
			line = line.rstrip()
			array = line.split(" ")
			if "lose" in array:
				value = -1*int(array[3])
			else:
				value = int(array[3])
			people[array[0],array[-1][0:-1]] = value
			names.append(array[0])
			names.append(array[-1][0:-1])
	recursive(names,people)

def recursive(names,people):
	names=list(set(names))
	permutations = list(itertools.permutations(names))
	happinessResult=[]
	for perm in permutations:
		i=0
		happiness=0
		while True:
			happiness += people[perm[i],perm[i+1]]
			i += 1
			if i+1 == len(perm):
				happiness += people[perm[i],perm[0]]
				break
		permReversed = list(reversed(perm))
		i=0
		while True:
			happiness += people[permReversed[i],permReversed[i+1]]
			i += 1
			if i+1 == len(perm):
				happiness += people[permReversed[i],permReversed[0]]
				break
		happinessResult.append(happiness)
	# pprint(happinessResult)
	print("Min : {}\n Max : {}".format(min(happinessResult),max(happinessResult)))


Main()
