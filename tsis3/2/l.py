n = int(input())
d = {}

for i in range(n):
    x, y = input().split()
    d[x] = y
    d[y] = x

s = input()
print(d[s])