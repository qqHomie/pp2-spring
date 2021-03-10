from collections import Counter
a = open('text.txt', 'r')
text = a.read().split()
res = Counter(text)
print(res)


# print(*sorted(res.keys(), key = res.get, reverse = True), sep='\n')


# from collections import Counter
# def word_count(fname):
#         with open(fname) as f:
#                 return Counter(f.read().split())

# print("Number of words in the file :",word_count("text.txt"))