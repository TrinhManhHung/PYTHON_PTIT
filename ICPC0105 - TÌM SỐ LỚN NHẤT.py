from math import *

test = int(input())
while test > 0:
    test -= 1
    s = input()
    num_s = ""
    for word in s:
        if word.isdigit():
            num_s += word
        else:
            num_s += " "
    
    list = map(int, num_s.split())
    max_numbers = max(list)
    print(max_numbers)