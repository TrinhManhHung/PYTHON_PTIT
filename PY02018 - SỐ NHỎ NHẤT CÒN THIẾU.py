
n = int(input())
arr = list(map(int, input().split()))

dem = [0] * 30002
dem[0] = 1
for num in arr:
    dem[num] = 1
for i in range(0, len(dem)):
    if dem[i] == 0:
        print(i)
        break
    