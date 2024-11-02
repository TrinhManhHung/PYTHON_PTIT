from math import *

def check(n):
    s1 = str(n)
    s2 = s1[::-1]
    return s1 == s2 and len(s1) >=2 

n, m = map(int, input().split())
arr = []

for N in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)

max_values = 0
for i in range(n):
    for j in range(m):
        if check(arr[i][j]):
            max_values = max(max_values, arr[i][j])

if max_values == 0: print("NOT FOUND")
else:
    print(max_values)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == max_values:
                print(f"Vi tri [{i}][{j}]")


'''
6 4
23 21 77 10
13 13 22 14
28 29 28 23
29 77 11 19
16 26 24 21
13 25 77 77
'''