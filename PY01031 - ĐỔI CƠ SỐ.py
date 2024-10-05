#chuyen so n sang he co so b
def Change(n, b) :
    res = ""
    while n != 0:
        m = n % b
        if m >= 10:
            res += str(chr(55 + m))
        else:
            res += str(m)
        n //= b
    
    res = res[::-1]
    return res

test = int(input())
while test > 0:
    test -= 1
    n, b = map(int, input().split())
    print(Change(n, b))