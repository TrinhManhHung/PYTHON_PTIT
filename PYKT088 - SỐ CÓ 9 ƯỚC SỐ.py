from math import *

def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return primes

n = int(input())
m = int(sqrt(n))
prime = sieve_of_eratosthenes(m)
cnt = 0

for i in range(0, len(prime)):
    if(prime[i] ** 8 <= n):
        cnt += 1
    for j in range(i+1, len(prime)):
        if (prime[i] ** 2) * (prime[j] ** 2) <= n:
            cnt += 1
        else:
            break

print(cnt)
