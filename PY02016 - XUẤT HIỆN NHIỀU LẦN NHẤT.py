from math import *

test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    nums = list(map(int, input().split()))

    frequency_dict = {}  # Đổi tên biến từ dict sang frequency_dict

    for num in nums:
        if num not in frequency_dict:
            frequency_dict[num] = 1
        else:
            frequency_dict[num] += 1

    max_frequency = max(frequency_dict.values())

    if max_frequency <= n / 2:
        print("NO")
    else:
        res = 1000001
        for key, value in frequency_dict.items():  # Lặp qua các cặp key-value
            if value == max_frequency:
                res = min(res, key)
        print(res)
