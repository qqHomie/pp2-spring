from collections import Counter

input = open('input.txt', 'r')

s = input.read()
s = s.split()

cnt = Counter(sorted(s))
print(*sorted(cnt.keys(), key=cnt.get, reverse = True), sep='\n')