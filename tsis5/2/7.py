s = 'The World of DOTA!'
lowcnt = 0
upcnt = 0
for i in s:
    if i.islower():
        lowcnt += 1
    elif i.isupper():
        upcnt += 1
print('Upper case characters: %s'%str(upcnt), 'Lower case characters: %s'%str(lowcnt), sep='\n')