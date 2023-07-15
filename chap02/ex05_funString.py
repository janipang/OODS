class funString():

    def __init__(self, string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self) :
        return len(self.string)

    def changeSize(self):
        resized = ""
        for i in range(len(self.string)):
            if (self.string[i].isupper()):
                resized += chr(ord(self.string[i]) + (ord('a') - ord('A')))
            elif (self.string[i].islower()):
                resized += chr(ord(self.string[i]) + (ord('A') - ord('a')))
            else:
                resized += self.string[i]
        return resized

    def reverse(self):
        reversed = ""
        for i in range (len(self.string) - 1, -1, -1):
            reversed += self.string[i]
        return reversed

    def deleteSame(self):
        deleted = ""
        for alpha in self.string:
            if alpha not in deleted:
                deleted += alpha
        return deleted


str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())