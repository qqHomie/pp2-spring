f = open('test.txt', 'r')
text = f.readlines()
text = [i.strip('\n') for i in text]
print(text)