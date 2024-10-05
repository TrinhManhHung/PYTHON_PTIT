from math import *

def check(s1, s2):
    return s1 == s2

test = int(input())
cnt = 1
while cnt <= test:
    str1 = input()
    str2 = input()
    str1 = sorted(str1)
    str2 = sorted(str2)
    print("Test ", cnt, ": ", sep = "", end = " ")
    if check(str1, str2):
        print("YES")
    else :
        print("NO")
    cnt += 1

'''
4
testing
intestg
abc
aabbbcccc
abcabcbcc
aabbbcccc
abc
xyz
'''

