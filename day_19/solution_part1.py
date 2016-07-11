from pprint import pprint

transition={}
text=""
combinations=[]

with open("fileTransitions.txt")as dataFile:
	for line in dataFile:
		line = line.rstrip()
		if line.split(" ")[0] in transition:
			transition[line.split(" ")[0]].append(line.split(" ")[2])
		else:
			transition[line.split(" ")[0]]=[line.split(" ")[2]]
with open("input.txt")as dataFile:
	text = dataFile.readline().rstrip()

pprint(transition)
print(25*"=")
for index,char in enumerate(text):
	if char in transition:
		print(char)
		for replacement in transition[char]:
			newComb = text[:index]+replacement+text[index+1:]
			print("\t=> {}".format(replacement))
			combinations.append(newComb)
	if index+1<len(text):
		s=text[index:index+2]
		if s in transition:
			print(s)
			for replacement in transition[s]:
				print("\t=> {}".format(replacement))
				newComb = text[:index]+replacement+text[index+2:]
				combinations.append(newComb)

print("Number of combinations is {}".format(len(combinations)))
combinations = set(combinations)
print("Number of distinct combinations is {}".format(len(combinations)))