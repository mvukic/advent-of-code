from hashlib import md5
import re

code="ckczppom"
x=1
while True:
    codeNew ="{}{}".format(code,str(x))
    md5_hash=md5(codeNew.encode('utf-8')).hexdigest()   
    if re.match(r"^[0]{5}[^0].*",md5_hash):
        print("Match found: {}".format(md5_hash))
        print ("Number is: {}".format(x))
        break
    x +=1