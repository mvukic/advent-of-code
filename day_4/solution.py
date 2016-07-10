from hashlib import md5
import re

code="ckczppom"
x=1
regexPart1 = r'^[0]{5}[^0].*'
regexPart2 = r'^[0]{6}[^0].*'
while True:
    codeNew ="{}{}".format(code,str(x))
    md5_hash=md5(codeNew.encode('utf-8')).hexdigest()   
    if re.match(regexPart2,md5_hash):
        print("Match found: {}".format(md5_hash))
        print ("Number is: {}".format(x))
        break
    x +=1