a = int(input())
b = int(input())
n = 1
m = 1
s = a - b
v = 1
for i in range(1, a + 1):
    n *= i
for i in range(1, b + 1):
    m *= i
for i in range(1, s + 1):
    v *= i
print(n//(m*v))