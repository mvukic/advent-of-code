from pprint import pprint

transition={}
text=""

def Main():
	with open("fileTransitions.txt")as dataFile:
		for line in dataFile:
			line = line.rstrip()
			if line.split(" ")[0] in transition:
				transition[line.split(" ")[0]].append(line.split(" ")[2])
			else:
				transition[line.split(" ")[0]]=[line.split(" ")[2]]
	with open("input.txt")as dataFile:
		text = dataFile.readline().rstrip()
	steps=0
	while True:
		(text,steps) = combs(text,steps)
		if text == "e":
			print("found e after {} steps".format(steps))
			break

def combs(result,steps):
	# print(result,steps)
	pprint(transition)
	for i in list(reversed(range(len(result)))):
		string = result[i:len(result)]
		print("Searching {}".format(string))
		for (k,v) in transition.items():
			if string in v and len(result) == 1:
				print("found value {} in {} with key {}".format(string,v,k))
				print("Returning ({} , {})".format(result[:i]+k,steps+1))
				return (result,steps+1)
			if string in v and k != "e":
				print("found value {} in {} with key {}".format(string,v,k))
				print("Returning ({} , {})".format(result[:i]+k,steps+1))
				return (result[:i]+k,steps+1)
		
Main()