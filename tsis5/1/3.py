f = open('text.txt', 'a')
n = "he world is the Earth and all life on it"
f.write(n)
f.close()
f = open('text.txt', 'r')
text = f.read()
print(text)