from math import *
class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a
    def tichMaTran(self):
        arr2 = [[0 for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                arr2[j][i] = self.a[i][j]
        res = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.m):
                    res[i][j] += self.a[i][k] * arr2[k][j]
        return res

if __name__ == '__main__':
    t = int(input())
    for T in range(t):
        nm = []
        while len(nm) < 2:
            nm.extend(list(map(int, input().split())))
        n = nm[0]
        m = nm[1]

        nums = []
        if (len(nm) > 2):
            for i in range(2, len(nm)):
                nums.append(nm[i])
        while len(nums) < n*m:
            nums.extend(list(map(int, input().split())))

        idx = 0
        arr = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                arr[i][j] = nums[idx]
                idx+=1

        matrix = Matrix(n, m, arr)
        res = matrix.tichMaTran()
        for row in res:
            print(" ".join(map(str, row)))


'''
1
2  2
1  
2
3  4
'''