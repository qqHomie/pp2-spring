a = input().split()
for i in range(len(a)):
    if int(a[i]) != 0:
        print(a[i], end = ' ')
for i in range(len(a)):
    if int(a[i]) == 0:
        print(a[i], end = ' ')