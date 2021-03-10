import os

os.chdir('20th')

for i in range(26):
    with open(chr(65+i) + '.txt', 'w') as f:
        f.write('')