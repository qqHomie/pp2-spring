f = open('text.txt', 'r')
lines = f.readlines()
n = 2
for i in lines[-n:]:
  print(i)