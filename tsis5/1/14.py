with open('text.txt', 'r') as f1:
  text1 = f1.readlines()
with open('test.txt', 'r') as f2:
  text2 = f2.readlines()

text1 = [i.strip('\n') for i in text1]
text2 = [i.strip('\n') for i in text2]

for i, j in (zip(text1, text2)):
    print(f'{i} {j}')
    
# print(text1)