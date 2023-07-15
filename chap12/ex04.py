print("*** String Rotation ***")

src = list(map(str, input("Enter 2 strings : ").split(' ')))

text = src[:]
def rightrotate(str1, n):
    temp = str1 + str1
    l = len(str1)
    return temp[n :l+n]

def leftrotate(str1, n):
    return rightrotate(str1, len(str1)-n)

round = 0
while (text != src or round == 0):
    text[0] = leftrotate(text[0], 1)
    text[1] = rightrotate(text[1], 1)
    round += 1
    if (round <= 5):
        print(round, end = ' ')
        print(text[0], end = ' ')
        print(text[1], end = '\n')
if (round > 6):
    print(" . . . . . ")
if (round > 5):
    print(round, end = ' ')
    print(text[0], end = ' ')
    print(text[1], end = '\n')
print("Total of  " + str(round) + " rounds.")