from shutil import copyfile

copyfile('text.txt', 'test.txt')
f = open('test.txt', 'r')

print(f.read())

'''
with open('text.txt', 'r') as f:
  text = f.copy()
  f.close()
a = open('test.txt', 'w')
a.write(text)
a.close()
a = open('test.txt', 'r')
print(a.read())
'''