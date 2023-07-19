class Queue:
	def __init__(self):
		self.queue = []
	def is_empty(self):
		if len(self.queue) <= 0:
			return 1
		return 0
	def put(self, obj):
		self.queue.append(obj)
		
	def put_at(self, index, obj):
		print("bf: ", end = '')
		print(row, end = '')
		self.queue.insert(index, obj)
		print("   af: ", end = '')
		print(row)
		
	def get(self):
		return self.queue.pop(0)
	def rear(self):
		if len(self.queue) == 0:
			return None
		return self.queue[-1]
	def front(self):
		if len(self.queue) == 0:
			return None
		return self.queue[0]
	def __len__(self):
		return len(self.queue)
	def __repr__(self):
		return str(self.queue)

command = list(map(str, input("Enter Input : ").split(',')))
row = Queue()
xrow = Queue()
for ele in command:
	mode = str(ele[:2])
	
	# print("mode:" + mode)
		
	if mode == "EN":
		id = int(ele[3:])
		row.put(id)
	if mode == "ES":
		id = int(ele[3:])
		xrow.put(id)
	if mode == 'D':
		# print(row)
		# print(xrow)
		if xrow.is_empty():
			if row.is_empty():
				print("Empty")
			else:
				print(row.get())
		else:
			print(xrow.get())
			
	