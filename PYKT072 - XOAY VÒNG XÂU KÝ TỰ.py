from math import *

check = True
arr = []
arr.append(0)

n = int(input())
s1 = input()

for i in range(n-1):
    s = input()
    if s == s1: arr.append(0)
    else:
        checkExist = False
        for j in range(1, len(s)):
            tmp = s[j:] + s[:j]
            if tmp == s1: 
                checkExist = True
                arr.append(j)
                break

        if checkExist == False: check = False

if check == False: print(-1)        
else: 
    arr.sort()

    res = 1000
    for i in range(0, len(arr)):
        cost = 0
        for j in range(0, len(arr)):
            if arr[j] > arr[i]:
                cost += arr[j] - arr[i]
            elif arr[j] < arr[i]:
                cost += len(s1) - (arr[i] - arr[j])
        res = min(res, cost)
    
    print(res)


'''
4
xzzwo
zwoxz
zzwox
xzzwo

3
aa
aa
ab
'''
