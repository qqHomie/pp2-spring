import os

text = open('text.txt', 'r')
# text.close()
if text.closed:
    print('yes')
else:
    print('no')