# Chapter : 1 - item : 3 - Reading E-book
print("*** Reading E-Book ***")
text = list(map(str, input("Text , Highlight : ").split(',')))

for alpha in text[0]:
    if alpha == text[1]:
        print('[' + alpha + ']', end = '')
    else:
        print(alpha, end = '')