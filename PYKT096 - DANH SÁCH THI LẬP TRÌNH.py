from math import *
from functools import cmp_to_key

mp = dict()

class Team:
    def __init__(self, id, name, school):
        self.id = 'Team' + f'{id:02d}'
        self.name = name
        self.school = school

    def __str__(self):
        return f'{self.name} {self.school}'

class SinhVien:
    def __init__(self, id, name, idTeam):
        self.id = 'C' + f'{id:03d}'
        self.name = name
        self.team = mp[idTeam]
    def __str__(self):
        return f'{self.id} {self.name} {self.team}'

def cmp(a, b):
    if a.name < b.name: return -1
    return 1
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        team = Team(i+1, input(), input())
        mp[team.id] = team

    n = int(input())
    arr = []
    for i in range(n):
        sv = SinhVien(i+1, input(), input())
        arr.append(sv)
    arr.sort(key = cmp_to_key(cmp))
    for x in arr:
        print(x)
'''
2
BAV_MIS
Banking Academy of Vietnam
FTU Knights1
Foreign Trade University
6
Le Trung Toan
Team01
Nguyen Trinh Quoc Long
Team01
Giang Minh Tung
Team01
Nguyen Hang Giang
Team02
Nguyen Thanh Nhan
Team02
Nguyen Viet Duc
Team02
'''