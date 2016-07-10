
visited_houses={}
with open("input.txt") as dataFile:
	directions=dataFile.readline().rstrip()
	santaLoc=(0,0)
	roboSantaLoc=(0,0)
	visited_houses[(0,0)]=2
	for index,direction in enumerate(directions):
		if index % 2 == 0:
			# print("SANTA {}".format(direction))
			if direction=="<":
				santaLoc=(santaLoc[0]-1,santaLoc[1])
			elif direction==">":
				santaLoc=(santaLoc[0]+1,santaLoc[1])
			elif direction=="^":
				santaLoc=(santaLoc[0],santaLoc[1]+1)
			else:
				santaLoc=(santaLoc[0],santaLoc[1]-1)
			if santaLoc in visited_houses:
				visited_houses[santaLoc] +=1
			else:
				visited_houses[santaLoc]=1
		else:
			# print("ROBO-SANTA {}".format(direction))
			if direction=="<":
				roboSantaLoc=(roboSantaLoc[0]-1,roboSantaLoc[1])
			elif direction==">":
				roboSantaLoc=(roboSantaLoc[0]+1,roboSantaLoc[1])
			elif direction=="^":
				roboSantaLoc=(roboSantaLoc[0],roboSantaLoc[1]+1)
			else:
				roboSantaLoc=(roboSantaLoc[0],roboSantaLoc[1]-1)
			if roboSantaLoc in visited_houses:
				visited_houses[roboSantaLoc] +=1
			else:
				visited_houses[roboSantaLoc]=1

print("Number of houses visited is: {}".format(len(visited_houses)))