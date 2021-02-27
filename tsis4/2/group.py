import re

s = input()
pattern = re.compile(r'\d?')
res = []
print(len(res))
res.append(re.match(pattern, s))
for i in res:
    print(i)
    break