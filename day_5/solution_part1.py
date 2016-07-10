number_of_nice_strings=0

with open("input.txt") as input:
    for line in input:
        line=line.rstrip()
        #chack vowels
        num_of_vowels=0
        vowels=["a","e","i","o","u"]
        vowels_dict={}
        for vowel in vowels:
            if vowel in line:
                vowels_dict[vowel] = line.count(vowel)
        for (k,v) in vowels_dict.items():
            num_of_vowels +=v
        #check repeatable letters
        repeatable_letters={}
        for i in range(len(line)):
            if i == len(line)-1:
                break
            # print("Letter is : {}".format(line[i]))
            if line[i] == line[i+1]:
                # print("Repeat of letter: {}".format(line[i]))
                repeatable_letters[line[i]]=1
        #chack if does not contain the fallowing
        contains_not_wanted=False
        not_wanted=["ab","cd","pq","xy"]
        for nw in not_wanted:
            if nw in line:
                contains_not_wanted=True
                break;
        print("{} has {} vowels.".format(line,num_of_vowels))
        print("{} has {} repeating letters.".format(line,len(repeatable_letters)))
        print("{} contains unwanted substrings: {}".format(line,contains_not_wanted))
        if num_of_vowels >=3 and not contains_not_wanted and len(repeatable_letters)>0:
            number_of_nice_strings +=1
            print("{} is nice.".format(line))
        else:
            print("{} is bad.".format(line))
print("Number of good strings is : {}".format(number_of_nice_strings))