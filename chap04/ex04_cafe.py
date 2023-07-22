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

print(" ***Cafe***")
command = list(map(str, input("Log : ").split('/')))

customer_id = 0
for i in range(len(command)):
    command[i] = list(map(int, command[i].split(',')))
    customer_id += 1
    command[i].append(customer_id)
    
# print(command)

q1 = Queue()
q2 = Queue()
serve = []
run_time = 0
wait_max = 0
cus_wait = 0

if command[0][0] == 0: q1.put(command.pop(0))
if command[0][0] == 0: q2.put(command.pop(0))
wait = 0

while not (q1.is_empty() and q2.is_empty() and len(command) == 0):
    run_time += 1
    if not q1.is_empty():
        if q1.front()[1] == run_time:
            serve.append(q1.get())
                
    if not q2.is_empty():
        if q2.front()[1] == run_time:
            serve.append(q2.get())
    
    serve.sort()
    while len(serve) > 0:
        receive = serve.pop(0)
        print(f"Time {run_time} customer {receive[2]} get coffee")
            
    if q1.is_empty() and len(command) > 0:
        if command[0][0] <= run_time:
            cmd = command.pop(0)
            wait = run_time - cmd[0]
            if wait > wait_max:
                wait_max = wait
                cus_wait = cmd[2]
            cmd[1] += run_time
            q1.put(cmd)
            
    if q2.is_empty() and len(command) > 0:
        if command[0][0] <= run_time:
            cmd = command.pop(0)
            wait = run_time - cmd[0]
            if wait > wait_max:
                wait_max = wait
                cus_wait = cmd[2]
            cmd[1] += run_time
            q2.put(cmd)
            
    # print(f"Time {run_time}\tq1: {q1}, q2: {q2}, command: {command}")
if (wait_max > 0):
        print(f"The customer who waited the longest is : {cus_wait}")
        print(f"The customer waited for {wait_max} minutes")
else:
        print("No waiting")