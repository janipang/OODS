class Stack:
	def __init__(self):
		self.stack = []
	
	def is_empty(self):
		if len(self.stack) <= 0:
			return 1
		return 0

	def push(self, obj):
		self.stack.append(obj)
	
	def pop(self):
		if self.is_empty():
			print(-1)
			return
		return self.stack.pop()
	
	def peek(self):
		if len(self.stack) == 0:
			return None
		return self.stack[-1]
	
	def __len__(self):
		return len(self.stack)
	
	def __str__(self):
		return str(self.stack)

def is_char(alpha):
    return alpha.isupper() or alpha.islower()

def priority(operation):
    operation = str(operation)
    if operation == "^":
        return 4
    elif operation in "*/":
        return 3
    elif operation in "+-":
        return 2
    elif operation == "(":
        return 1
    else:
        return -1

def in_to_post(infix,st):
    postfix = ""
    operators = "^*/+-"
    for var in infix:
        if is_char(var):
            postfix += var
        elif var in operators:
            if priority(var) > priority(st.peek()):
                st.push(var)
            else:
                while priority(var) <= priority(st.peek()):
                    postfix += st.pop()
                st.push(var)
        elif var == '(':
            st.push(var)
        elif var == ')':
            while st.peek() != '(':
                postfix += st.pop()
            st.pop()
    while not st.is_empty():
        postfix += st.pop()
    print("Postfix : " + postfix)
        

inprut = str(input("Enter Infix : "))
st = Stack()
in_to_post(inprut, st)
                