
str = input().lower()

check = True
for c in str:
    if not ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '.' or c == '_'):
        check = False
        break

if check:
    if str[len(str) - 3:] == '.py':
        print("yes")
    else:
        print("no")

else:
    print("no")