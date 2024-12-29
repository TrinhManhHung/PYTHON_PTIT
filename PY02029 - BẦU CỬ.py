from math import *

if __name__ == "__main__":
#    for T in range(int(input())):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        fre = dict()
        maxx = 0
        for x in a:
            fre[x] = fre.get(x, 0) + 1
            maxx = max(fre[x], maxx)

        arrFre = list(fre.values())
        arrFre.sort()
        maxx2 = -1
        for i in range(len(arrFre)-1, 0, -1):
            if arrFre[i] < maxx:
                maxx2 = arrFre[i]
                break
        if maxx2 == -1: print("NONE")
        else:
            res = 1000
            arr = list(fre.keys())
            for x in arr:
                if fre[x] == maxx2:
                    res = min(res, x)
            print(res)

'''
10 4
2 3 1 2 3 4 1 2 3 2
'''