from math import *

test = int(input())
while test > 0 :
    test -= 1
    s = input()
    tam = 1
    ans = ""
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            ans += str(tam) + s[i-1]
            tam = 1
        else:
            tam += 1
    
    ans += str(tam) + s[len(s) - 1]
    print(ans)


'''
3
AACDDPQ
11111147g
1111111111
'''
