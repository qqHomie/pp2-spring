import re

with open('text.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()

name_company = re.search(r'Филиал\sТОО\s\w+\s\w+', text)
BIN = re.search(r'\d{12}?', text)
items = re.findall(r'\d+\.\n(.*)', text)
cnt = re.findall(r'(\d),\d{3}', text)
price = re.findall(r'x\s([\d\s]+,\d+)', text)
TotalPrice = re.findall(r'x\s[\d\s]+,\d+\n(.*)', text)
date = re.search(r'(\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2})', text)
address = re.search(r'г\.(.*)', text)


print('1. Name of the company: ' + name_company.group())
print('2. BIN number: ' + BIN.group())

print('3. For each item:')
for i in range(len(items)):
    print('\t' + str(i+1) + ')' + '-'*20)
    print('\t   1. Title --> ' + items[i])
    print('\t   2. Cout --> (' + cnt[i] + ')')
    print('\t   3. Unit Price --> (' + price[i] + ')')
    print('\t   4. Total Price --> (' + TotalPrice[i] + ')')

print('4. Date --> ' + date.group())
print('5. Address --> ' + address.group())