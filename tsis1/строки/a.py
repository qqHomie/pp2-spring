a = input()
print(a[2])
print(a[-2])
print(a[0:5])
print(a[0:len(a)-2])
b = ""
for i in range(len(a)):
    if i%2==0:
        b += a[i]
print(b)
c = ""
for i in range(len(a)):
    if i%2!=0:
        c += a[i]
print(c)
print(a[::-1])
def r(a):
    return a[::-1]
x = ""
for i in range(len(a)):
    if i%2==0:
        x += r(a)[i]
print(x)
print(len(a))
