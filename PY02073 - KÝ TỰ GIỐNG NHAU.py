from math import *

t = int(input())
for T in range(t):
    n = int(input())
    x, y, z = map(int, input().split())
    dp = [0] * (n*2+2)
    dp[1] = x
    for i in range(2, 2*n+1):
        if i % 2 == 0:
            dp[i] = min(dp[i-1] + x, dp[int(i/2)] + z)
        else:
            dp[i] = min(dp[i-1] + x, dp[int((i+1)/2)] +y +z)
    
    print(dp[n])
'''
6
4
4 2 10 1
2
1 3
2
6 1
3
1 4 2
5
1 2 3 4 3
12
4 31 25 50 30 20 34 46 42 16 15 16
'''
