from pprint import pprint


def Loop(row,col):
	step=1
	while True:
		steps = list(range(1,step+1))
		for i,j in zip(list(reversed(steps)),steps):
			if (i,j) == (1,1):
				prevVal=20151125
			else:
				nextValue = (prevVal*252533)%33554393
				prevVal=nextValue
			# print("({},{}) = {}".format(i,j,prevVal))
			if (i,j) == (row,col):
				print("Row: {} Column: {} => {}".format(row,col,prevVal))
				return
		step +=1

Loop(3010,3019)