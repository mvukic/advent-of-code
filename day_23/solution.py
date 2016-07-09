from pprint import pprint

commands=[]

with open("input.txt",'r') as dataFile:
	for index,line in enumerate(dataFile):
		line=line.rstrip()
		array = line.split(" ")
		if len(array) == 3:
			if "+" in array[2]:
				offset=int(array[2][1:])
			else:
				offset=-1*int(array[2][1:])
			cmd={
				"index":index,
				"type":"jmp_cond",
				"cmd":array[0],
				"op":array[1][:-1],
				"offset":offset
				}
		else:
			if array[0] == "jmp":
				if "+" in array[1]:
					offset=int(array[1][1:])
				else:
					offset=-1*int(array[1][1:])
				cmd={
					"index":index,
					"type":"jmp_uncond",
					"cmd":array[0],
					"offset":offset
				}
			else:
				cmd={
					"index":index,
					"type":"reg_op",
					"cmd":array[0],
					"op":array[1]
				}
		commands.append(cmd)
# pprint(commands)
(regA,regB,commandCounter) = (0,0,0)

while regCounter < len(commands):
	command = commands[commandCounter]
	if command["type"] == "jmp_cond":
		if command["cmd"] == "jio":
			if command["op"] == "a":
				if 
		else:


