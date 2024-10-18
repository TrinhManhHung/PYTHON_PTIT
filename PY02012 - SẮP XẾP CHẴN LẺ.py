from math import *

n = int(input())
arr = []
while len(arr) < n:
    tam = list(map(int, input().split()))
    arr.extend(tam)

evenNums = []
oddNums = []
for x in arr:
    if x % 2 == 0:
        evenNums.append(x)
    else:
        oddNums.append(x)

evenNums.sort()
oddNums.sort(reverse = True)

for x in arr:
    if x % 2 == 0:
        print(evenNums[0], end = " ")
        evenNums.pop(0)
    else:
        print(oddNums[0], end = " ")
        oddNums.pop(0)

'''
2
7
1 2 3 2 3 1 3
5
1 1 3 3 2
'''