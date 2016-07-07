import re
from pprint import pprint

aunts={}
match={}
for i in range(1,501):
	match[i]=0
	aunts[i]={
		"children":None,
		"cats":None,
		"samoyeds":None,
		"pomeranians":None,
		"akitas":None,
		"vizslas":None,
		"goldfish":None,
		"trees":None,
		"cars":None,
		"perfumes":None
	}

with open("input.txt",mode='r') as dataFile:
	x=1
	for sue in dataFile:
		sue=sue.rstrip()
		sue = sue[sue.index(":")+2:]
		array = sue.split(",")
		for desc in array:
			l=desc.split(":")[0].strip()
			r=int(desc.split(":")[1].strip())
			aunts[x][l]=r
		x += 1
for (k,v) in aunts.items():
	if v["children"]==3:
		match[k]+=1
	if v["cats"]==7:
		match[k]+=1
	if v["samoyeds"]==2:
		match[k]+=1
	if v["pomeranians"]==3:
		match[k]+=1
	if v["akitas"]==0:
		match[k]+=1
	if v["vizslas"]==0:
		match[k]+=1
	if v["goldfish"]==5:
		match[k]+=1
	if v["trees"]==3:
		match[k]+=1
	if v["cars"]==2:
		match[k]+=1
	if v["perfumes"]==1:
		match[k]+=1

maxMatches = max(list(match.values()))
for (k,v) in match.items():
	if v == max(list(match.values())):
		print("Aunt #{} sent the gift.".format(k))
		break