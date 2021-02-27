import re
s = input()
pattern = '\W'
result = re.split(pattern, s)
for i in result:
    print(i)