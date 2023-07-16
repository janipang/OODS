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
			return -1
		return self.stack[-1]

	def max(self):
		if self.is_empty():
			return -1
		return max(self.stack)
	
	def __len__(self):
		return len(self.stack)
	
	def __str__(self):
		return str(self.stack)

def count_tree(cmd):
	passed_tree = Stack()
	mao_hed = Stack()
	look_back = Stack()
	for ele in cmd:
		mode = ele[0]
		if mode == 'A':
			new_tree = int(ele[2:])
			passed_tree.push(new_tree)
		if mode == 'B':
			count = 0
			while not passed_tree.is_empty():
				if passed_tree.peek() > look_back.max():
					count += 1
				look_back.push(passed_tree.pop())
			while not look_back.is_empty():
				passed_tree.push(look_back.pop())
			print(count)
		if mode == 'S':
			while not passed_tree.is_empty():
				if passed_tree.peek() % 2 == 0:
					if passed_tree.peek() > 1:
						mao_hed.push(passed_tree.pop() - 1)
				else:
					mao_hed.push(passed_tree.pop() + 2)
			while not mao_hed.is_empty():
				passed_tree.push(mao_hed.pop())
    
command = list(map(str, input("Enter Input : ").split(',')))
count_tree(command)