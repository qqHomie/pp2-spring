n = int(input())
a = []
for i in range(1, n//2 + 1):
    if n%i == 0:
        a.append(i)
if n == sum(a, 0):
    print('%s is perfect number'%str(n))
else:
    print('Sorry, but you are not right for us')