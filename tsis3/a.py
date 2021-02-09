a = input().split() #input with spaces
# a = [int(i) for i in input().split()]
for i in range(0, len(a), 2): #(start, till, step)
    print(a[i], end = ' ')