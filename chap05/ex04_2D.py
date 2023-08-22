class node:
    def __init__(self,data):
        self.data = data
        self.vlink = Vlink()
        
        self.next = None
        self.prev = None
        
        self.deep = None
        self.pdeep = None
        
class Snode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Vlink:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, new):
        if self.head == None:
            self.head = self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
    
class link:
    def __init__(self):
        self.head = None
        self.tail = None
    def next_node(self,new):
        if self.head == None:
            self.head = self.tail = new
        else:
            if self.search(new.data
                           ) == None:
                new.prev = self.tail
                self.tail.next = new
                self.tail = new
    def search(self,data):
        runner = self.head
        while runner.data != data:
            if runner == self.tail:
                return None
            runner = runner.next
        return runner
    def next_secondary_node(self,n,new):
        runner = self.search(n)
        runner.vlink.append(new)
        
    def show_all(self):
        runner = self.head
        while runner != None:
            print(f"{runner.data} : ", end = '')
            Vrunner = runner.vlink.head
            while Vrunner != None:
                print(f"{Vrunner.data},", end = '')
                Vrunner = Vrunner.next
            print("")
            runner = runner.next
                
        
inp = input("input : ").split(",")
l = link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0],Snode(h[1]))
l.show_all()