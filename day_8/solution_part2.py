import re

unescaped=0
escaped=0
i=0

with open("input.txt") as dat:
	for line in dat:
		line=line.rstrip()
		unescaped+=len(line)
		escaped+=len(re.escape(line))+2

print("Result is: {}".format(escaped-unescaped))
