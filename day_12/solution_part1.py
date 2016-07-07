import re

with open('input.txt', encoding='utf-8') as data:
	line = data.readline().rstrip()
	allNumbers = re.findall(r'([-]?\d*)',line)
	sum=0
	for v in allNumbers:
		try:
			sum+=int(v)
		except ValueError:
			pass
	print("Sum is : {}".format(sum))