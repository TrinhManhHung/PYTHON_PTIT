from math import *


s = input()
arr = []
while len(s) >= 2:
    num = int(s[0:2])
    if num not in arr:
        arr.append(num)
    s = s[2:]

for x in arr:
    print(x, end = ' ')