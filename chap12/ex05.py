class MyInt:
    def __init__(self, num):
        self.num = num
        
    def isPrime(self):
        if (self.num < 2):
            return False
        for dvd in range(2, self.num):
            if (not(self.num % dvd)):
                return False
        return True
    
    def showPrime(self):
        if (self.num < 2):
            print(" !!!A prime number is a natural number greater than 1", end = '')
        for i in range (2, self.num + 1):
            if (MyInt(i).isPrime()):
                print(" " + str(i), end = '')
        print()
        
    def __sub__(self, other):
        return self.num - other.num // 2

print(" *** class MyInt ***")
num_list = list(map(int, input("Enter 2 number : ").split(' ')))

a = MyInt(num_list[0])
b = MyInt(num_list[1])

print(str(a.num) + " isPrime : " + str(a.isPrime()))
print(str(b.num) + " isPrime : " + str(b.isPrime()))
print("Prime number between 2 and " + str(a.num) + " :", end = '')
a.showPrime()
print("Prime number between 2 and " + str(b.num) + " :", end = '')
b.showPrime()
print(str(a.num) + " - " + str(b.num) + " = " + str(a - b))
    