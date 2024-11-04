from math import *

n = int(input())
a = list(map(int, input().split()))

a.sort()
maxOfTwo = max(a[0] * a[1], a[n-2] * a[n-1])
maxOfThree = max(a[0] * a[1] * a[2], a[n-1] * a[n-2] * a[n-3], a[0] * a[1] * a[n-1], a[n-1] * a[n-2] * a[0])

print(max(maxOfTwo, maxOfThree))

'''
'''