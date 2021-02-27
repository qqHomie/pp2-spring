n, m = input().split()
a = set()
b = set()
for i in range(int(n)):
    x = int(input())
    a.add(x)
for i in range(int(m)):
    y = int(input())
    b.add(y)

c = set(a.intersection(b))
print(len(c))
c1 = list(c)
c1.sort()
for i in range(len(c1)):
    print(c1[i], end = ' ')
print()

d = set(a.difference(b))
print(len(d))
d1 = list(d)
d1.sort()
for i in d1:
    print(i, end = ' ')
print()

e = set(b.difference(a))
print(len(e))
e1 = list(e)
e1.sort()
for i in e1:
    print(i, end = ' ')