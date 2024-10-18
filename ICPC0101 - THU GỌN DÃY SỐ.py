
n = int(input())
arr = list(map(int, input().split()))

stack = []
i = 0
while i < len(arr):
    if len(stack) != 0 and (stack[len(stack) - 1] + arr[i]) % 2 == 0:
        stack.pop()
    else:
        stack.append(arr[i])
    i += 1
print(len(stack))
    