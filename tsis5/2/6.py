n = 5
def check(n):
    if n in range(1, 10):
        print('%s has found in this range'%str(n))
    else:
        print('This number is not here')
check(n)