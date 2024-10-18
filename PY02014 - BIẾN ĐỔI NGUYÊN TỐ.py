from math import *

prime_list = [-1] * 10001

def checkPrime():
    for i in range(2, 10001):
        isPrime = False
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                isPrime = True
                break
        if isPrime == False: prime_list[i] = 0

checkPrime()     
n = int(input())
arr = list(map(int, input().split()))

res = 0
for x in arr:
    left = x
    right = x
    while left >= 2 and prime_list[left] != 0:
        left -= 1 
    while right <= 10000 and prime_list[right] != 0:
        right += 1 
    
    res = max(res, min(x - left, right - x))

print(res)
'''
8
13 5 8 7 9 15 26 34
8
'''