import os

text = os.stat('text.txt')
print(text.st_size)