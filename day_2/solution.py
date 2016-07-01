
final_size=0
with open("input.txt") as input:
    for line in input:
        line = line.rstrip()
        l=int(line.split("x")[0])
        w=int(line.split("x")[1])
        h=int(line.split("x")[2])
        dim=(2*l*w,2*w*h,2*h*l)
        size = sum(dim)+min(dim)/2
        final_size+=size
print("Final size is: {}".format(final_size))