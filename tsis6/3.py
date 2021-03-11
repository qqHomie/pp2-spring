a = [1, 2, 3, 4, 5]
def mult(mylist):
    res = 1
    for i in mylist:
        res *= i
    return res
print(mult(a))