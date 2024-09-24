from math import *

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1, 1):
        if(n % i == 0): return False
    return True


rows, cols = map(int, input().split())

matrix = []

for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(rows):
    for j in range(cols):
        if isPrime(matrix[i][j]):
            print(1, end = " ")
        else:
            print(0, end = " ")
    print()
