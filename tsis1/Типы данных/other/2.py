a = int(input())
if a<=0:
    print((a-1)*abs(a)//2 + 1)
else:
    print(a*(a+1)//2)