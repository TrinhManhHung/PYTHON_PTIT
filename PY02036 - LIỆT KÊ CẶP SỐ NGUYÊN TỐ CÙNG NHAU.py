
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
for i in range(0, n-1):
    for j in range(i+1, n):
        if gcd(nums[i], nums[j]) == 1:
            print(nums[i], nums[j])
