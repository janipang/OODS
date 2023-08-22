class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.refered = 0
    def isHead(self):
        return self.refered == 0
    def __repr__(self):
        string = str(self.data) + " ref=" + str(self.refered) + " "
        return string
    
class Nodes:
    def __init__(self):
        self.ele = []
        self.head = []
        self.ints = []
        self.arranged = []
        self.path_buff = []
    def search(self,data):
        for runner in self.ele:
            if runner.data == data:
                return runner
        return None
    def update_head(self):
        self.head = []
        for runner in self.ele:
            if runner.refered == 0:
                self.head.append(runner)
    def connect(self, data, ref_to):
        if self.search(ref_to) == None:
            self.ele.append(Node(ref_to))
        end = self.search(ref_to)
        end.refered += 1
        if self.search(data) == None:
            self.ele.append(Node(data))
        first = self.search(data)
        first.next = end
    def update_intersec(self):
       for runner in self.ele:
           if runner.refered > 1:
               self.ints.append(runner)
    #for runner in self.ele
    def count_from(self, node):
        length = 1
        start_node = node
        path_buff = [start_node]
        while node.next != None and node.next not in path_buff:
            length += 1
            path_buff.append(node.next)
            node = node.next
        return length
    def delete_ints(self):#########
        for runner in self.ele:
            if runner in self.ints:
                if runner.next != None:
                    runner.next.refered -= 1
            elif runner.next in self.ints:
                runner.next = None
    def remove_none_from_head(self):
        while None in self.head:
            self.head.remove(None)
    def sort_head(self):
        self.head.sort(key=get_head_val)
    def sort_ints(self):
        self.ints.sort(key=get_ints_val)
    def delete_level(self):
        for runner in self.head:
            self.arranged.append(runner.data)
            if runner.next == None or runner.next in self.ints:
                self.head[self.head.index(runner)] = None
            else:
                self.head[self.head.index(runner)] = runner.next
    def print_arranged(self):
        i = 0
        while i < len(self.arranged):
            print(self.arranged[i], end='')
            i+=1
            if i < len(self.arranged):
                print(" -> ", end='')
            
            
def get_head_val(node):
    return node.data
def get_ints_val(node):
    return node.data
                
                
connectand = list(data.split('>') for data in input("Enter edges: ").split(','))
a = Nodes()
for cnt in connectand:
    a.connect(int(cnt[0]), int(cnt[1]))
    
a.update_intersec()

a.sort_ints()
for runner in a.ints:
    print(f"Node({runner.data}, size={a.count_from(runner)})")
    
a.delete_ints()
a.update_head()
if a.ints == []:
    print("No intersection")
    exit()

a.sort_head()
while a.head != []:
    # print(f"head left: {a.head}")
    a.delete_level()
    a.remove_none_from_head()

print("Delete intersection then swap merge:")
a.print_arranged()