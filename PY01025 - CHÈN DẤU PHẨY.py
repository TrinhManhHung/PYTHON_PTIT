from math import *
#input
n = input()
res = ""
cnt = 0
#tinh toan
cnt = 0
for i in range(len(n)-1, -1, -1) :
    cnt += 1
    res += n[i]
    if(cnt % 3 == 0):
        res += ','
#output
if len(n) % 3 == 0:
    res = res[:len(res)-1]
res = res[::-1]
print(res)
