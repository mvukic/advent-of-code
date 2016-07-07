import json
from pprint import pprint

def n(j):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([n(j) for j in j])
    if type(j) != dict:
        return 0
    if 'red' in j.values():
        return 0
    return n(list(j.values()))

with open('input.txt', encoding='utf-8') as data:
	line = data.readline().rstrip()
	parsed=json.loads(line)
	pprint(parsed)
	print("Sum is : {}".format(n(parsed)))