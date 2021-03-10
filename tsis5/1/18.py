with open('text.txt', 'r') as f:
    text = f.read()
    text.replace(",", " ")
    print(len(text.split()))
 