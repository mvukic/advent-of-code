unparsed=0
parsed=0

with open("input.txt") as dat:
	for line in dat:
		line=line.rstrip()
		unparsed += len(line)
		parsed += len(eval(line))

print("Result is: {}".format(unparsed-parsed))

