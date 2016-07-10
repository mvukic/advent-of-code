from pprint import pprint

reindeers=[]
distances={}
points={}
def Main():
	with open("input.txt") as dataFile:
		for line in dataFile:
			line = line.rstrip()
			array = line.split(" ")
			reindeers.append({"name":array[0],"speed":int(array[3]),"flyTime":int(array[6]),"restTime":int(array[-2]),"flyTimeCount":0,"restTimeCount":0,"state":None})
	for i in range(1,2503+1):
		for reindeer in reindeers:
			distances[reindeer["name"]]=GetDistance(reindeer,i)
		maxDist = max([t[1] for t in distances.values()])
		for name,val in distances.items():
			if val[1] == maxDist:
				if name in points:
					points[name] +=1
				else:
					points[name] = 1
	maxPoints = sorted(points,key=points.get,reverse=True)
	# pprint (maxPoints)
	print("{} flew {} and has {} points.".format(maxPoints[0],distances[maxPoints[0]][1],points[maxPoints[0]]))

def GetDistance(reindeer,endTime):
	distance = 0
	seconds = 0
	while True:
		for time1 in range(1,reindeer["flyTime"]+1):
			distance += reindeer["speed"]
			if seconds == endTime:
				return ("FLYING",distance)
			seconds +=1
		for time2 in range(1,reindeer["restTime"]+1):
			if seconds == endTime:
				return ("RESTING",distance)
			seconds +=1
			
if __name__ == "__main__":
	print("Calculating...")
	Main()