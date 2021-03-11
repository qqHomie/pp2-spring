s = input()
char_list = []
s = s.lower()
for i in s:
    if i not in char_list and i.isalpha():
        char_list.append(i)
if len(char_list) == 26:
    print('Panagram')
else:
    print('No')