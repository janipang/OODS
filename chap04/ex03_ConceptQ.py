class Queue:
	def __init__(self):
		self.queue = []
  
	def is_empty(self):
		if len(self.queue) <= 0:
			return 1
		return 0

	def put(self, obj):
		self.queue.append(obj)
		
	def get(self):
		return self.queue.pop(0)

	def front(self):
		if len(self.queue) == 0:
			return None
		return self.queue[0]

	def __len__(self):
		return len(self.queue)

	def __repr__(self):
		return str(self.queue)

command = list(map(str, input("input : ").split(',')))
row = Queue()
d_error = 0
i_error = 0
counter = 0

for cmd in command:
	print("Step : " + cmd)
	mode = cmd[0]
	try:
		times = int(cmd[1:])
	except ValueError:
		mode = 'K'
  
	if mode == 'D':
		for i in range(times):
			if row.is_empty():
				d_error += 1
			else:
				row.get()
		print("Dequeue : ", end = '')
	elif mode == 'E':
		for i in range(times):
			row.put('*' + str(counter))
			counter += 1
		print("Enqueue : ", end = '')
	else:
		i_error += 1
	print(row)
	print("Error Dequeue : " + str(d_error))
	print("Error input : " + str(i_error))
	print("--------------------")
	
