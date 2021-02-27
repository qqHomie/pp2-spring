import re
n = int(input())
a = list()
for i in range(n):
    a.append(input())
pattern = '(\+?\.?|\-?\.?|\+?|\-?|\.?|\d+?)\d+?\.?\d+$'
for i in a:
    if re.match(pattern, i):
        print(True)
    else:
        print(False)