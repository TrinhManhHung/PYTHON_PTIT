
test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    stack = []
    for i in range(0, len(arr)):
        while len(stack) != 0 and arr[i] >= arr[stack[-1]]:
            stack.pop()
        if len(stack) == 0:
            print(i + 1, end = ' ')
        else: 
            print(i - stack[-1], end = ' ')
        stack.append(i)
    print()