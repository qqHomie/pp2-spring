a = open('perfect.in', 'r')
text = a.readlines()
cnt = []
for i in range(len(text)):
  cnt.append(i+1)
print('Number of lines is:', len(cnt))



# def file_lengthy(fname):
#         with open(fname) as f:
#                 for i, l in enumerate(f):
#                         pass
#         return i + 1
# print("Number of lines in the file: ",file_lengthy("text.txt"))