values={}

with open("input.txt") as dat:
    for line in dat:
        line=line.rstrip()
        parts=line.split(" ")
        if len(parts) == 5:
            #var op var -> var
        elif len(parts) == 4:
            #op var -> var
        elif len(parts) == 3:
            #var -> var