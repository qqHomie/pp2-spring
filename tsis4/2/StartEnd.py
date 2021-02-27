import re
s = input()
n = input()
key = re.compile(n)
res = key.search(s)
if not res:
    print("(-1, -1)")
while res:
    print("(" + str(res.start()) + ",", str(res.end() - 1) + ")")
    res = key.search(s, res.start() + 1)