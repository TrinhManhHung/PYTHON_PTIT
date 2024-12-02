from decimal import *
from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other_point):
        distancee = sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        formatted_num =  f"{distancee:.4f}"
        return formatted_num
    
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
