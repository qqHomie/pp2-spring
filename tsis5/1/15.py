from random import randint
with open('text.txt', 'r') as f1:
  text1 = f1.readlines()
print(text1[randint(0, len(text1))])