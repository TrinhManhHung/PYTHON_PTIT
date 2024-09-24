#chuyen so n sang he co so b
def check(s):
    s = s.strip()
    arr = s.split(".")
    if len(arr) != 4:
        return False 
    for x in arr:
        if(not x.isdigit() or int(x) < 0 or int(x) > 255):
            return False
    
    return True
    

test = int(input())
while test > 0:
    test -= 1
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")