from math import *


s = input()
arr = []
fre = {}
while len(s) >= 2:
    num = int(s[0:2])
    if num not in arr:
        arr.append(num)
    fre[num] = fre.get(num, 0) + 1
    s = s[2:]

for x in arr:
    print(x, fre[x])