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
        self.root, path = self._insert(self.root, data)
        print(path)

    def _insert(self, root, data):
        if root is None:
            return Node(data), "*"
        if data < root.data:
            root.left, path = self._insert(root.left, data)
            return root, "L" + path
        else:
            root.right, path = self._insert(root.right, data)
            return root, "R" + path
    
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)
    
T = BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for i in inp:
    root = T.insert(i)