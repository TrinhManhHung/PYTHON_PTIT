
def sort_by_sum(x):
    sum = 0
    while x != 0:
        sum += x % 10
        x //= 10
    return sum

test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.sort(key = sort_by_sum)
    for x in arr:
        print(x, end = ' ')
    print()
    