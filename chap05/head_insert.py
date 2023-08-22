class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

#insert at tail
class List:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self, data):
        new = Node(data)
    
        the_node = self.head
        if the_node == None:
            self.head = new
        else:
            while the_node.next != None:
                the_node = the_node.next
            the_node.next = new
            self.size += 1
    
    def head_insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
    
    def __str__(self):
        text = ""
        the_node = self.head
        while the_node != None:
            text += str(the_node) + ' '
            the_node = the_node.next
        return text
    
    
a = List()
a.append('a')
a.append('b')
a.append('c')
a.head_insert('x')

print(a)
print(a.size)
