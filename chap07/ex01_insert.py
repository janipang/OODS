class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        self._insert(data, self.root)
            
    def _insert(self, data, current):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
                return
            self._insert(data, current.left)
        else:
            if current.right is None:
                current.right = Node(data)
                return
            self._insert(data, current.right)            
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(T.root)