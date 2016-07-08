from pprint import pprint
import itertools

def Main():
	trans={}
	transList=[]
	with open("input.txt","r") as dataFile:
		for line in dataFile:
			line = line.rstrip()
			array = line.split(" ")
			transList.append(array[0])
			transList.append(array[2])
			trans[array[0],array[2]]=int(array[4])
			trans[array[2],array[0]]=int(array[4])
	recursive(transList,trans)

def recursive(t,trans):
	t=list(set(t))
	permutations = list(itertools.permutations(t))
	distances=[]
	for perm in permutations:
		i=0
		distance=0
		while True:
			if (perm[i],perm[i+1]) in trans:
				distance += trans[perm[i],perm[i+1]]
			i += 1
			if i+1 == len(perm):
				break
		distances.append(distance)
	print("Shortest distance is {}".format(min(distances)))


Main()