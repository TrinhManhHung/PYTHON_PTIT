from math import *

n = int(input())
arr = []
data_map = dict()
cnt = 0
for N in range(n):
    arr.append(input().strip())
    if N == 0 or arr[N-1] == "":
        cnt = 0
    elif(arr[N] == ""):
        data_map[arr[N-cnt-1]] = cnt
    else: cnt += 1

data_map[arr[n-cnt-1]] = cnt
for keys, values in data_map.items():
    print(keys, ": ", values, sep = "")



'''
9
Home/accommodation
What kind of housing/accommodation do you live in?
Who do you live with?
How long have you lived there?

Study
Describe your education
What is your area of specialization?
Why did you choose to study that major?

Home/accommodation: 3
Study: 3
'''