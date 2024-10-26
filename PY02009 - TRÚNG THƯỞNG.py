test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    list = [0] * 1005
    maxx = 0
    for i in range(n):
        x = int(input())
        list[x] += 1
        maxx = max(maxx, list[x])
    
    for i in range(1001):
        if list[i] == maxx:
            print(i)
            break