from math import *

primes = [1] * 10005
list_prime = []
def sangnt():
    primes[0] = primes[1] = 0
    for i in range(2, 101):
        if primes[i] == 1:
            for j in range(i * 2, 10001, i):
                primes[j] = 0
    
    for i in range(0, 10005):
        if primes[i] == 1:
            list_prime.append(i)

sangnt()
n, x = map(int, input().split())
cnt = 0

while n > 0:
    print(x, end = " ")
    x += list_prime[cnt]
    n -= 1
    cnt += 1
print(x, end = " ")