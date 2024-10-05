
test = int(input())

while test > 0:
    test -= 1
    s = input()
    if(s[0] == s[len(s)-1]):
        print("YES")
    else:
        print("NO")
