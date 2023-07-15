class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, obj):
        self.stack.append(obj)
    
    def remove(self):
        return self.stack.pop()
        
    def top(self):
        return self.stack[-1]
    
    def __len__(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)

a = Stack()
parenth = list(map(str, input("Enter Input : ")))
# for each in parenth:
#     if each == ')' and a.stack[-1] == '(':
#         a.remove()
#     elif each == ']' and a.stack[-1] == '[':
#         a.remove()
#     else:
#         a.push(each)

odd = Stack()
while len(parenth) > 0:
    if parenth[0] == '(' or parenth[0] == '[':
        state = 1
        for str in parenth:
            if (parenth[0] == '(' and str == ')') or (parenth[0] == '[' and str == ']'):
                parenth.remove(str)
                parenth.pop(0)
                state = 0
                break
        if state: odd.push(parenth.pop(0))
    else:
        odd.push(parenth.pop(0))

# print(len(a))
# for a in a.stack: print(a, end = ' ')
# if not len(a):
#     print("Perfect ! ! !")


print(len(odd))
# for o in odd.stack: print(o, end = ' ')
if not len(odd):
    print("Perfect ! ! !")
