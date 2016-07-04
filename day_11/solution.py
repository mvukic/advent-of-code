notWanted = ["i","o","l"]

def RecursiveIncrement(array,index):
	if index == len(array):
		return array
	if array[index] == 'z':
		array[index] = 'a'
		return RecursiveIncrement(array,index+1)
	else:
		array[index] = chr(ord(array[index])+1)
		return array

def IfHasSameLetterTwice(password):
	hasOne=False
	firstLetter = ""
	hasTwo=False
	for i,v in enumerate(password):
		if i >= len(password)-1:
			hasOne = False
			break
		if password[i+1] == v:
			hasOne = True
			firstLetter=v
			break

	for i,v in enumerate(password):
		if i >= len(password)-1:
			hasTwo = False
			break
		if v != firstLetter and password[i+1] == v:
			hasTwo = True
			break
	return hasOne and hasTwo

def CheckIncreasingArray(password):
	for i,v in enumerate(password):
		if i >= len(password)-2:
			return False
		if password[i+1] == chr(ord(v)+1) and password[i+2] == chr(ord(v)+2):
			return True

def IfContainsIOL(password):
	for c in notWanted:
		if c in password:
			return True
	return False

def Check(password):
	return CheckIncreasingArray(password) and not IfContainsIOL(password) and IfHasSameLetterTwice(password)

def GetNextPassword(currPass):
	revCurrPass = list(reversed(currPass))
	newPass = list(reversed(RecursiveIncrement(revCurrPass,0)))
	return newPass

def Main():
	currPass = list("currentPassword")
	currPass = GetNextPassword(currPass)
	while not Check(currPass):
		newPass = GetNextPassword(currPass)
		currPass.clear()
		currPass=list(newPass)
	print("Password found: {}".format("".join(currPass)))

Main()


