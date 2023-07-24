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

def check_map_correction(width, height, map):
    my_pos = 0
    if len(map1) != height:
        print("Invalid map input.")
        exit(0)
    for line in map:
        my_pos += line.count('F')
        if len(line) != width:
            print("Invalid map input.")
            exit(0)
    if my_pos != 1:
        print("Invalid map input.")
        exit(0)
        
def get_start_pos(map):
    for line in map:
        if 'F' in line:
            return (line.index('F'), map.index(line))

# def not_ever_pass(x_pos, y_pos):
#     if (x_pos, y_pos) in passed_path:
#         return 0
#     return 1
        
def look_around():
    global finding_way
    x_pos, y_pos = finding_way.front()[0], finding_way.front()[1]
    if y_pos > 0:
        if map1[y_pos - 1][x_pos] == 'O':
            print("Found the exit portal.")
            exit()
        if map1[y_pos - 1][x_pos] == '_':
            finding_way.put((x_pos, y_pos - 1))
            map1[y_pos - 1][x_pos] = 'X'
    if x_pos < width - 1:
        if map1[y_pos][x_pos + 1] == 'O':
            print("Found the exit portal.")
            exit()
        if map1[y_pos][x_pos + 1] == '_':
            finding_way.put((x_pos + 1, y_pos))
            map1[y_pos][x_pos + 1] = 'X'
    if y_pos < height - 1:
        if map1[y_pos + 1][x_pos] == 'O':
            print("Found the exit portal.")
            exit()
        if map1[y_pos + 1][x_pos] == '_':
            finding_way.put((x_pos, y_pos + 1))
            map1[y_pos + 1][x_pos] = 'X'
    if x_pos > 0:
        if map1[y_pos][x_pos - 1] == 'O':
            print("Found the exit portal.")
            exit()
        if map1[y_pos][x_pos - 1] == '_':
            finding_way.put((x_pos - 1, y_pos))
            map1[y_pos][x_pos - 1] = 'X'
    finding_way.get()
    if not finding_way.is_empty():
        print(f"Queue: {finding_way}")
    else:
        print("Cannot reach the exit portal.")
        
        
            
width, height, map1 = list(data.split(',') for data in input("Enter width, height, and room: ").split(' '))
width, height = int(width[0]), int(height[0])
for i in range(len(map1)):
    map1[i] = list(map1[i])

check_map_correction(width, height, map1)
# for line in map1: print(line)
finding_way = Queue()
passed_path = []
finding_way.put(get_start_pos(map1))
print(f"Queue: {finding_way}")
while finding_way:
	look_around()
    