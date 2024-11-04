from math import *

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0: return False
    return True

n, m = map(int, input().split())

arr = []
for N in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)

maxPrime = 0
for i in range(n):
    for j in range(m):
        if isPrime(arr[i][j]):
            maxPrime = max(maxPrime, arr[i][j])

if maxPrime == 0: print("NOT FOUND")
else:
    print(maxPrime)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == maxPrime:
                print(f"Vi tri [{i}][{j}]")
