from math import *

if __name__ == "__main__":
    # t = int(input())
    # for T in range(t):
        n = int(input())
        arr = [[0 for _ in range(n)] for _ in range(n)]
        nums = []
        while(len(nums) < n*n):
            nums.extend(list(map(int, input().split())))
        idx = 0
        for i in range(n):
            for j in range(n):
                arr[i][j] = nums[idx]
                idx += 1
        upperHalf = 0
        belowHalf = 0
        for i in range(n):
            for j in range(n):
                if i > j:
                    belowHalf += arr[i][j]
                elif i < j:
                    upperHalf += arr[i][j]

        k = int(input())
        if abs(upperHalf - belowHalf) <= k:
            print("YES")
        else:
            print("NO")
        print(abs(upperHalf - belowHalf))


'''
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
'''