a = open('text.txt', 'r')
lines = []
text = a.readlines()
for i in text:
  lines.append(i)
print(lines)