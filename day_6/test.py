import re
line="turn off 660,55 through 986,197"
m = re.match(r"^[a-zA-Z ]*([0-9]{1,3}),([0-9]{1,3})[a-zA-Z ]*([0-9]{1,3}),([0-9]{1,3})",line)
start=(int(m.group(1)),int(m.group(2)))
end=(int(m.group(3)),int(m.group(4)))
print(end[0]-start[0])
print("{} {}".format(str(start[0]),str(start[1])))
print("{} {}".format(str(end[0]),str(end[1])))
for i in range(5,9):
    print(i)