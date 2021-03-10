a = open('text.txt', 'r')
text = a.read().split()
max_len = 0
for i in text:
  if len(i) > max_len:
    max_len = len(i)
for i in text:
  if len(i) == max_len:
    print(i)
    break

'''
a = open('text.txt', 'r')
text = a.read().split()
max_len = len(max(text, key=len))
for i in text:
    if len(i) == max_len:
        print(i)
        break
'''