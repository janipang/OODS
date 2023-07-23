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

command = list(data.split(' ') for data in input("Enter Input : ").split(','))
# print(command)
q = Queue()

for cmd in command:
    mode = cmd[0]
    if mode == 'E':
        ele = cmd[1]
        print(f"Add {ele} index is {len(q)}")
        q.put(ele)
    elif mode == 'D':
        if q.is_empty():
            print(-1)
        else:
            ele = q.get()
            print(f"Pop {ele} size in queue is {len(q)}")
        
if q.is_empty():
    print("Empty")
else:
    print(f"Number in Queue is :  {q}")