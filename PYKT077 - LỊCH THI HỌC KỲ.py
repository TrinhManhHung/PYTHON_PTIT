from math import *
from functools import cmp_to_key

mp = {}
class MonHoc:
    def __init__(self, idTH, idMH, date, time, group):
        self.idTH = "T" + f'{idTH:03d}'
        self.idMH = idMH
        self.name = mp[idMH]
        self.date = date
        self.time = time
        self.group = group

    def __str__(self):
        return f'{self.idTH} {self.idMH} {self.name} {self.date} {self.time} {self.group}'

def cmp(a, b):
    datea = a.date
    ya = int(datea[6:])
    ma = int(datea[3:5])
    da = int(datea[0:2])
    dateb = b.date
    yb = int(dateb[6:])
    mb = int(dateb[3:5])
    db = int(dateb[0:2])
    if(ya != yb): return ya - yb
    if(ma != mb): return ma - mb
    if(da != db): return da - db
    timea = a.time
    ha = int(timea[0:2])
    mia = int(timea[3:])
    timeb = b.time
    hb = int(timeb[0:2])
    mib = int(timeb[3:])
    if(ha != hb): return ha - hb
    if(mia != mib): return mia - mib
    if(a.idMH < b.idMH): return -1
    return 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    for _ in range(n):
        id = input()
        sub = input()
        mp[id] = sub

    arr = []
    for i in range(m):
        a, b, c, d = map(str, input().split())
        mh = MonHoc(i+1, a, b, c, d)
        arr.append(mh)
    arr.sort(key = cmp_to_key(cmp))
    for x in arr:
        print(x)
'''
2 10
INT1155
Tin hoc co so 2
INT1339
Ngon ngu lap trinh C++
INT1155 25/11/2021 08:00 01
INT1155 04/12/2021 08:00 02
INT1155 04/12/2021 13:30 03
INT1155 25/11/2021 13:30 04
INT1155 25/11/2021 15:00 05
INT1339 25/11/2021 08:00 01
INT1339 25/11/2021 08:00 02
INT1339 04/12/2021 13:30 03
INT1339 04/12/2021 13:30 04
INT1339 04/12/2021 15:00 05
'''