
floor=0

with open("input.txt") as input:
    line = input.readlines()[0].rstrip()
    for direction in line:
        if direction == "(":
            floor +=1
        else:
             floor -=1

print("Floor: {}".format(floor))