from pprint import pprint

reindeers=[]
distances={}
def Main():
	with open("input.txt") as dataFile:
		for line in dataFile:
			line = line.rstrip()
			array = line.split(" ")
			reindeers.append({"name":array[0],"speed":int(array[3]),"flyTime":int(array[6]),"restTime":int(array[-2]),"flyTimeCount":0,"restTimeCount":0,"state":None})
	for reindeer in reindeers:
		distances[reindeer["name"]]=GetDistance(reindeer)
	pprint(distances)
	sort = sorted(distances,key=distances.get,reverse=True)
	print("{} flew {} km.".format(sort[0],distances[sort[0]]))
	print("{} flew {} km.".format(sort[-1],distances[sort[-1]]))

def GetDistance(reindeer):
	distance = 0
	seconds = 0
	while True:
		for time1 in range(1,reindeer["flyTime"]+1):
			distance += reindeer["speed"]
			if seconds == 2503:
				return ("FLYING",distance)
			seconds +=1
		for time2 in range(1,reindeer["restTime"]+1):
			if seconds == 2503:
				return ("RESTING",distance)
			seconds +=1
			
if __name__ == "__main__":
	Main()