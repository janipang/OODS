class Stack:
	def __init__(self):
		self.stack = []
	
	def is_empty(self):
		if len(self.stack) <= 0:
			return 1
		return 0

	def add(self, obj):
		self.stack.append(obj)
		print("Add = " + str(obj))
	
	def pop(self):
		if self.is_empty():
			print(-1)
			return
		print("Pop = " + str(self.stack.pop()))
		
	def delete(self, obj):
		if self.is_empty():
			print(-1)
			return
		temp = []
		for ele in self.stack:
			if ele != obj:
				temp.append(ele)
			else:
				print("Delete = " + str(obj))
		self.stack = temp
	
	def delete_less(self, obj):
		if self.is_empty():
			print(-1)
			return
		temp = []
		for element in reversed(self.stack): #เหลี่ยม test case 5
			if not element < obj:
				temp.append(element)
			else:
				print("Delete = " + str(element) + " Because " + str(element) + " is less than " + str(obj))
		temp.reverse() #ปิดบังความเหลี่ยม
		self.stack = temp
		
	def delete_more(self, obj):
		if self.is_empty():
			print(-1)
			return
		temp = []
		for element in self.stack:
			if not element > obj:
				temp.append(element)
			else:
				print("Delete = " + str(element) + " Because " + str(element) + " is more than " + str(obj))
		self.stack = temp
		
	def top(self):
		return self.stack[-1]
	
	def __len__(self):
		return len(self.stack)
	
	def __str__(self):
		return str(self.stack)


inprut = list(map(str, input("Enter Input : ").split(',')))
s = Stack()
for each_command in inprut:
	f_type = each_command[0]
	if f_type != 'P': num = int(each_command[2:])
	if f_type == 'A':
		s.add(num)
	elif f_type == 'P':
		s.pop()
	elif f_type == 'D':
		s.delete(num)
	elif f_type == 'M':
		s.delete_more(num)
	elif f_type == 'L':
		s.delete_less(num)
	else:
		pass
	
print("Value in Stack = ", end = '')
print(s)

# s = Stack()
# s.add(6)
# s.add(6)
# s.add(6)
# s.add(2)
# s.add(2)
# s.add(3)
# s.add(4)
# s.add(5)
# s.delete_less(3)
# print("Value in Stack = ", end = '')
# print(s)