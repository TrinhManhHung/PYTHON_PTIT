from math import *

s = input()
cntUpper = 0
cntLower = 0
for word in s:
    if (word >= 'a') and (word <= 'z'):
        cntLower += 1
    else :
        cntUpper += 1
    
if(cntUpper > cntLower):
    print(s.upper())
else :
    print(s.lower())