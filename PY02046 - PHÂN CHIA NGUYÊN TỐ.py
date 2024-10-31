from math import *

def isPrime(n):
    if(n < 2): return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

n = int(input())
nums = list(map(int, input().split()))

b = []
sumb = 0
for x in nums:
    if x not in b:
        b.append(x)
        sumb += x

idx = 0
curSum = 0
while idx < len(b):
    curSum += b[idx]
    if isPrime(curSum) and isPrime(sumb - curSum):
        print(idx)
        break
    idx += 1

if idx == len(b): print("NOT FOUND")

'''
10
3 6 7 3 4 7 3 6 4 4

10
3 6 7 3 5 7 3 6 6 7
'''
