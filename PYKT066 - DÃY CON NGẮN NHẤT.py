from math import *
from functools import cmp_to_key

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = []
        while len(arr) != n:
            tmp = list(map(int, input().split()))
            arr.extend(tmp)
        res = 1001
        for i in range(n):
            curgcd = arr[i]
            if curgcd == k:
                res = 1
                break
            for j in range(i+1, n):
                curgcd = gcd(curgcd, arr[j])
                if curgcd == k:
                    res = min(res, j - i + 1)
                    break
                elif curgcd < k: break

        if res == 1001: print(-1)
        else: print(res)

'''
3
8 3
6 9 7 10 12 24 36 27
4 3
2 4 6 8
4 6
1 2 3 6
'''