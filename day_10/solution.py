import sys

def count(startIndex,digit,array):
	index=startIndex+1
	num_of_repeat=1

	while(True):
		if index >= len(array):
			break
		if array[index] != digit:
			break
		num_of_repeat +=1
		index +=1
	return num_of_repeat

def workIt(array):
	index=0
	while(index < len(array)):
		repeats=count(index,array[index],array)
		final.append(str(repeats))
		final.append(array[index])
		index = index+repeats

def main():
	if len(sys.argv) < 2:
		print("USAGE:")
		print("\tpython3 solution.py number_of_iterations")
		exit(1)
	iteration = sys.argv[1]
	array = list("1113222113")
	for i in range(int(iteration)):
		workIt(array)
		array = list(final)
		final.clear()
	# print(array)
	print(len(array))

final=[]
main()