a = int(input())
b = int(input())
def p(a, b):
    if b == 0:
        return 1
    return p(a, b-1)*a
p(a, b)