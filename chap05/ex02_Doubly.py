class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return str(self.data)

#insert at tail
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def append(self, data):
        new = Node(data)
    
        the_node = self.head
        if the_node == None:
            self.head = new
            self.tail = new
        else:
            while the_node.next != None:
                the_node = the_node.next
            new.prev = the_node
            the_node.next = new
            # print(f"now: {new.data} prev: {new.prev}")
            self.tail = new
        self.size += 1
    
    def head_insert(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            self.tail = new
            self.size += 1
            return
        
        new.next = self.head
        self.head.prev = new
        self.head = new
        if self.tail == None:
            self.tail = new
        self.size += 1
        
    def insert(self, index, data):
        new = Node(data)
        if index not in range(self.size + 1):
            print("Data cannot be added")
            return
        if index == 0:
            self.head_insert(data)
            print(f"index = {index} and data = {data}")
        elif index == self.size:
            self.append(data)
            print(f"index = {index} and data = {data}")
        else:
            the_node = self.head
            index_counter = 0
            while index_counter != index:
                the_node = the_node.next
                index_counter += 1
            new.prev = the_node.prev
            new.next = the_node
            the_node.prev.next = new
            the_node.prev = new
            print(f"index = {index} and data = {new.data}")
            self.size += 1
        
    def remove(self, data):
        the_node = self.head
        index_counter = 0
        while the_node != None:
            if the_node.data == data:
                if index_counter == 0:
                    if self.size == 1:
                        self.head = None
                        self.tail = None
                    else:
                        the_node.next.prev = None
                        self.head = the_node.next
                        the_node.next = None
                elif index_counter == self.size - 1:
                    the_node.prev.next = None
                    self.tail = the_node.prev
                    the_node.prev = None
                else:
                    the_node.prev.next = the_node.next
                    the_node.next.prev = the_node.prev
                self.size -= 1
                print(f'removed : {data} from index : {index_counter}')
                return
            the_node = the_node.next
            index_counter += 1
        print("Not Found!")
    
    def isEmpty(self):
        return self.head == None

    def __str__(self):
        text = ""
        the_node = self.head
        while the_node != None:
            text += str(the_node)
            the_node = the_node.next
            if the_node != None:
                text += '->'
        return text
    
    def str_reverse(self):
        text = ""
        the_node = self.tail
        while the_node != None:
            text += str(the_node)
            the_node = the_node.prev
            if the_node != None:
                text += '->'
        return text
    
a = List()

command = list(data.strip().split(' ') for data in input("Enter Input : ").split(','))

for cmd in command:
    mode = cmd[0]
    if mode == "A":
        a.append(int(cmd[1]))
    elif mode == "Ab":
        a.head_insert(int(cmd[1]))
    elif mode == "I":
        data, index = cmd[1].split(':')
        # print(f'data, index: {data}, {index}')
        a.insert(int(data), int(index))
    elif mode == "R":
        a.remove(int(cmd[1]))
    
    
    print(f'linked list : ', end = '')
    print(a)
    
    print(f'reverse : ', end = '')
    print(a.str_reverse())
    
#I 1:1,I 0:0,I 0:1,I 0:2,I 3:-1,I -1:-1,I 10:5,I 2:0, A 20, Ab -3, R 10, R 0, R 1, R 2, R 0
#it's have space in A 20, Ab -3