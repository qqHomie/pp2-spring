n = int(input())
m = 1
s = 0
while n>0:
    m *= n%10
    s += n%10
    n //= 10
print(m-s)