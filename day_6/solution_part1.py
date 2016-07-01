import re

matrix={}
with open("input.txt") as dat:
    print("Initializing matrix to zeroes.")
    for i in range(1000):
        for j in range(1000):
            matrix[(i,j)]=0
    print("Setting lights...")
    for line in dat:
        line = line.rstrip()
        m = re.match(r"^[a-zA-Z ]*([0-9]{1,3}),([0-9]{1,3})[a-zA-Z ]*([0-9]{1,3}),([0-9]{1,3})",line)
        start=(int(m.group(1)),int(m.group(2)))
        end=(int(m.group(3)),int(m.group(4)))
        if "off" in line:
            # print("Turning off: {},{} -> {},{}".format(str(start[0]),str(start[1]),str(end[0]),str(end[1])))
            for i in range(start[0],end[0]+1):
                for j in range(start[1],end[1]+1):
                    matrix[(i,j)]=0
        elif "on" in line:
            # print("Turning on: {},{} -> {},{}".format(str(start[0]),str(start[1]),str(end[0]),str(end[1])))
            for i in range(start[0],end[0]+1):
                for j in range(start[1],end[1]+1):
                    matrix[(i,j)]=1
        else:
            # print("Toggling: {},{} -> {},{}".format(str(start[0]),str(start[1]),str(end[0]),str(end[1])))
            for i in range(start[0],end[0]+1):
                for j in range(start[1],end[1]+1):
                    matrix[(i,j)]=1-matrix[(i,j)]
counter=0
for k in matrix.keys():
    if matrix[k] == 1:
        counter +=1
print("Number of lights is: {}".format(counter))