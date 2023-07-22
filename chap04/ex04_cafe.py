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
			return [-1, -1, -1]
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
b1, b2 = Queue(), Queue()
run_time = 0
wait_max, cus_wait  = 0, 0

cmd = command.pop(0)
in_time, cook_time, customer_id = cmd[0], cmd[1], cmd[2]

def assign_order_to_barista(that_b):
    global in_time, cook_time, customer_id, cus_wait, wait_max, cmd
    if run_time >= in_time:
        # print(f"cmd: {cmd}")
        if run_time - in_time > wait_max:
            wait_max = run_time - in_time
            cus_wait = customer_id
        that_b.put(cmd)
        if len(command) > 0:
            cmd = command.pop(0)
            in_time, cook_time, customer_id = cmd[0], cmd[1], cmd[2]
        else:
            cmd = [-1, -1, -1]
        
while not (len(command) == 0 and b1.is_empty() and b1.is_empty()):
    while (b1.is_empty() or b2.is_empty()) and run_time >= in_time: #in_time >= runtime and barista is available
        # print(f"cmd: {cmd}")
        if run_time - in_time > wait_max:
            wait_max = run_time - in_time
            cus_wait = customer_id
        if b1.is_empty():
            b1.put(cmd)
        elif b2.is_empty():
            b2.put(cmd)
        cmd = command.pop(0)
        in_time, cook_time, customer_id = cmd[0], cmd[1], cmd[2]
    while ((b1.front()[1] == 0) or (b2.front()[1] == 0)):
        if b2.front()[1] == 0:
            receiver = b2.get()
            if len(command) >= 0:
                assign_order_to_barista(b2)
        elif b1.front()[1] == 0:
            receiver = b1.get()
            if len(command) >= 0:
                assign_order_to_barista(b1)
        print(f"Time {run_time} customer {receiver[2]} get coffee")
        
    # print(f"turnly {run_time}: b1 = {b1}, b2 = {b2}")
    b1.front()[1] -= 1 #decrease cook_time
    b2.front()[1] -= 1
    run_time += 1
    if b1.front()[0] == -1 and b2.front()[0] == -1:
        break
print(f"The customer who waited the longest is : {cus_wait}")
print(f"The customer waited for {wait_max - 1} minutes")
            
        


