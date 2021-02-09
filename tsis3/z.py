a = input().split()
b = int(input())
b = b % len(a)
if b > 0:
    for i in range(len(a)-b, len(a)):
        print(a[i], end = ' ')
    for i in range(0, len(a)-b):
        print(a[i], end = ' ')
elif b == 0:
    for i in range(len(a)):
        print(a[i], end = ' ')
else:
    for i in range(abs(b), len(a)):
        print(a[i], end = ' ')
    for i in range(0, abs(b)):
        print(a[i], end = ' ')
# 1 2 3 4 5 (b = 3)
# 3 4 5 1 2
