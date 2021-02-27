import re
n = int(input())
a = list()
for i in range(n):
    colors = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if colors:
        a.append(colors)
for i in range(len(a)):
    print(*a[i], sep='\n')