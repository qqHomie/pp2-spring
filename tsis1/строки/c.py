a = input()
x = ""
y = ""
if len(a)%2==0:
    for i in range(len(a)//2):
        x += a[i]
    for i in range(len(a)//2, len(a)):
        y += a[i]
    print(y+x)
else:
    for i in range(0, len(a)//2 + 1):
        x += a[i]
    for i in range(len(a)//2 + 1, len(a)):
        y += a[i]
    print(y+x)