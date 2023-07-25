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
            print(-1)
            return
        return self.stack.pop()
    
    def __len__(self):
        return len(self.stack)
    
    def __repr__(self):
        if self.is_empty(): return "Empty"
        string = ""
        for item in self.stack:
            string += (str(item) + ' ')
        return string
    
command = [item.split(' ') for item in input("Enter Input : ").split(',')]
st = Stack()

for cmd in command:
    if cmd[0] == 'A':
        print(f"Add = {st.push(int(cmd[1]))} and Size = {len(st)}")
    if cmd[0] == 'P':
        if st.is_empty():
            st.pop()
            continue
        print(f"Pop = {st.pop()} and Index = {len(st)}")

print(f"Value in Stack = {st}")