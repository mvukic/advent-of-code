
visited_houses={}
with open("input.txt") as input:
    directions=input.readlines()[0].rstrip()
    loc=(0,0) #EAST or WEST and NORTH or SOUTH
    visited_houses[loc]=1
    for direction in directions:
        if direction=="<":
            loc=(loc[0]-1,loc[1])
        elif direction==">":
            loc=(loc[0]+1,loc[1])
        elif direction=="^":
            loc=(loc[0],loc[1]+1)
        else:
            loc=(loc[0],loc[1]-1)
        if loc in visited_houses:
            visited_houses[loc] +=1
        else:
            visited_houses[loc]=1

print("Number of houses visited is: {}".format(len(visited_houses)))