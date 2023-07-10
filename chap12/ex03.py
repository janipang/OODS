print("*** String Rotation ***")

src = list(map(str, input("Enter 2 strings : ").split(' ')))
text = src
def leftrotate(s):
    tmp = s[1 : ] + s[0 : 1]
    return tmp

def rightrotate(s):
    tmp = s[0 : ] + s[1 : ]
    return tmp

round = 1
while (text != src):
    text[0] = leftrotate(text[0])
    text[1] = rightrotate(text[1])
    if (round <= 5):
        print(round, end = ' ')
        print(text[0], end = ' ')
        print(text[1], end = ' ')