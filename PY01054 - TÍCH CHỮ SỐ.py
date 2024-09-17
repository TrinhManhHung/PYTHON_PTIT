
test = int(input())
for i in range(test):
    n = input()
    res = 1
    for x in n:
        if x != '0':
            res *= int(x)
    
    print(res)
    