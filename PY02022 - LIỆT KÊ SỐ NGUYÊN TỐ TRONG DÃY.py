
from math import *

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
nums = list(map(int, input().split()))
primes = {}

for i in range(0, n):
    if isPrime(nums[i]):
        primes[nums[i]] = primes.get(nums[i], 0) + 1

for i in range(0, n):
    if primes.get(nums[i], 0) != 0:
        print(nums[i], primes.get(nums[i]))
        primes[nums[i]] = 0

