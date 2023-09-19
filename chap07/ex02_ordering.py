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
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        return root
    
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)

    def descending(self, node):
        if node is None:
            return
        if node.right is not None:
            self.descending(node.right)
        print(node.data, end=" ")
        if node.left is not None:
            self.descending(node.left)

    def ascending(self, node):
        if node is None:
            return
        if node.left is not None:
            self.ascending(node.left)
        print(node.data, end=" ")
        if node.right is not None:
            self.ascending(node.right)

T = BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for i in inp:
    root = T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------")
print("Descending: ", end="")
T.descending(T.root)
print()
print("Ascending: ", end="")
T.ascending(T.root)
print()