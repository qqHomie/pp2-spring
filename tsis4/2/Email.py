import re

n = int(input())

pattern_email = '<[a-zA-Z](\w|-|\.|_)+\@?[a-zA-Z]+\.[a-zA-Z]{1,3}>'

for i in range(n):
    x, y = input().split()
    email = re.match(pattern_email, y)
    if email:
        print(x, y)
