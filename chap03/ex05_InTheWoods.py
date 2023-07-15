class Stack():
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
		if self.is_empty():
			return None
		return self.stack[-1]
	
	def __len__(self):
		return len(self.stack)
	
	def __str__(self):
		return str(self.stack)

command = list(map(str, input("Enter Input : ").split(',')))

def count_tree(cmd):
    back_tree = Stack()
    mao_hed = Stack()
    for ele in cmd:
        mode = ele[0]
        if mode == 'A':
            pass
        if mode == 'B':
            pass
        if mode == 'S':
            pass