import re

n = int(input())

l = list()

for i in range(n):
    x = input()
    l.append(x)

pattern_number = '(7|8|9)(\d{9}$)'

for i in l:
    if re.match(pattern_number, i):
        print("YES")
    else:
        print("NO")