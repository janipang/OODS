class Stack:
    def __init__(self, stack = None):
        if stack == None:
            self.stack = []
        else:
            self.stack = stack
        
    def push(self, value):
        self.stack.append(value)
        return value
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return self.stack == []
        
    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()
    
    def __len__(self):
        return len(self.stack)
    
    def __repr__(self):
        if self.is_empty(): return "Empty"
        return str(self.stack)
    
st = Stack()
print(len(setattr))
    