with open('test.txt', 'w') as f:
  for i in range(26):
    f.write(str(i+1) + ')' + chr(65+i))
    f.write('\n')
with open('test.txt', 'r') as f:
  print(f.read())