char = []
with open('test.txt', 'r') as f:
    for i in f.read():
        if 'a'<=i<='z' or 'A'<=i<='Z':
            char.append(i)
print(char)