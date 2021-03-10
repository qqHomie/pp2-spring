f = open('test.txt', 'w')
numbers = ['777', '333', '666']
for i in numbers:
  f.write(i)
  f.write('\n')
f.close()
x = open('test.txt', 'r')
print(x.read())

'''
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('test.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('test.txt')
print(content.read())
'''