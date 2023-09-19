class Path:
    def __init__(self):
        self.path = []
    
    def append(self, data):
        self.path.append(data)
    
    def pop(self):
        return self.pop()
    
    def clear(self):
        self.path = []
    
    def sumVal(self):
        if self.path == []:
            return -3000000000
        return sum(self.path)
    
    def __str__(self):
        string = ""
        for num in self.path:
            string += str(num)
            string += " "
        return str(self.path)

cur_path = Path()
max_path = Path()
    
class BST:
    def __init__(self):
        self.tree = [999]
        self.length = 0

    def insert(self, data):
        self.tree.append(data)
        self.length += 1  
    
    def printTree(self):
        print(self.tree)

    def maxPath(self, i):
        global cur_path
        global max_path
        if i > self.length:
            cur_path.clear()
            i = i // 2
            while i > 0:
                cur_path.append(self.tree[i])
                i = i // 2
            cur_path.path.reverse()

            if cur_path.sumVal() >= max_path.sumVal():
                max_path.path = cur_path.path.copy()
            return
        
        self.maxPath(2*i)
        self.maxPath((2*i)+1)
        
T = BST()
inp = [int(i) for i in input('Enter tree: ').split()]
for i in inp:
    root = T.insert(i)
T.maxPath(1)
print(f"Maximum path: {max_path}")
