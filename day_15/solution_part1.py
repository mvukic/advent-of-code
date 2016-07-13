import re
from pprint import pprint
import itertools

def Main():
	ingredients={}
	combinations = []
	result={}
	with open('input.txt',mode='r') as data:
		for line in data:
			line=line.rstrip()
			nums = re.findall(r'([+-]?[0-9]{1,})',line)
			nums = [int(n) for n in nums]
			ingredients[line.split(":")[0]]={
				"capacity":nums[0],
				"durability":nums[1],
				"flavor":nums[2],
				"texture":nums[3],
				"calories":nums[4]
			}
	for comb in itertools.combinations(range(1,101),len(ingredients)):
		if sum(comb) == 100:
			for perm in itertools.permutations(comb):
				combinations.append(perm)
	for comb in combinations:
		(a,b,c,d) = (ingredients["Sprinkles"],ingredients["PeanutButter"],ingredients["Frosting"],ingredients["Sugar"])
		cap= comb[0]*a["capacity"]  +comb[1]*b["capacity"]  +comb[2]*c["capacity"]  +comb[3]*d["capacity"]
		dur= comb[0]*a["durability"]+comb[1]*b["durability"]+comb[2]*c["durability"]+comb[3]*d["durability"]
		fla= comb[0]*a["flavor"]    +comb[1]*b["flavor"]    +comb[2]*c["flavor"]    +comb[3]*d["flavor"]
		tex= comb[0]*a["texture"]   +comb[1]*b["texture"]   +comb[2]*c["texture"]   +comb[3]*d["texture"]
		if not (cap < 0 or dur < 0 or fla<0 or tex<0):
			result[comb] = cap*dur*fla*tex
			if result[comb] == 11171160:
				print (comb)
	sort = sorted(result,key=result.get,reverse=True)
	print("{} gives best score of {}".format(sort[0],result[sort[0]]))


if __name__ == "__main__":
	print("Calculating...")
	Main()
