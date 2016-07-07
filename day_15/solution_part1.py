import re
from pprint import pprint
import itertools

def WorkIt():
	print("")

def Main():
	ingredients={}
	with open('input.txt',mode='r') as data:
		for line in data:
			line=line.rstrip()
			nums = re.findall(r'([+-]?[0-9]{1,})',line)
			nums = [int(n) for n in nums]
			ingredients[line.split(":")[0]]=nums
	pprint(ingredients)
	for i in range(0,101):
		sumCap=ingredients['Sprinkles'][0]*i+ingredients['PeanutButter'][0]*(100-i)
		sumDur=ingredients['Sprinkles'][1]*i+ingredients['PeanutButter'][1]*(100-i)
		sumFlav=ingredients['Sprinkles'][2]*i+ingredients['PeanutButter'][2]*(100-i)
		sumTex=ingredients['Sprinkles'][3]*i+ingredients['PeanutButter'][3]*(100-i)
		mulAll=sumCap*sumDur*sumFlav*sumTex
		print("{},{} => {}*{}*{}*{} = {}".format(i,100-i,sumCap,sumDur,sumFlav,sumTex,mulAll))

Main()
