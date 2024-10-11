
n = int(input())
nums = list(map(float, input().split()))
nums.sort()

minx = nums[0]
maxx = nums[n - 1]
nums = [x for x in nums if x != minx and x != maxx]

res = sum(nums) / len(nums)
print(round(res, 2))