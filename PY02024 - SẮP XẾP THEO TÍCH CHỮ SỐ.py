
def mul_of_digits(x):
    res = 1
    while x != 0:
        res *= x % 10
        x //= 10
    return res

def sort_of_nums(x):
    return (mul_of_digits(x), x)
test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(key = sort_of_nums)
    for x in arr:
        print(x, end = ' ')
    print()
    