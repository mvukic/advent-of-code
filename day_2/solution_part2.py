ribbonSize=0
final_size=0
with open("input.txt") as input:
	for line in input:
		line = line.rstrip()
		(l,w,h)=line.split("x")
		(l,w,h) = (int(l),int(w),int(h))
		dim=(2*l*w,2*w*h,2*h*l)
		size = sum(dim)+min(dim)/2
		final_size+=size
		s = tuple(sorted((l,w,h)))
		ribbonSize += s[0]*2+s[1]*2 + l*w*h
print("Final size is: {}".format(final_size))
print("Required ribbon size is: {}".format(ribbonSize))
