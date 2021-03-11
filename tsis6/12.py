s = input()
def ispalindrom(mystr):
    s1 = ''.join(reversed(mystr))  # mystr[::-1] 
    if s1 == mystr:
        print('Cool')
    else:
        print('Sorry')
ispalindrom(s)