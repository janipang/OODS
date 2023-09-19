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
            
    def top_view(self, node):
        if node is None:
            return
        if node.left is not None and self.is_left_border(self.root.left, node.left):
        # if node.left is not None and node.left.data < self.root.data:
            self.top_view(node.left)
        print(node.data, end = " ")
        if node.right is not None and self.is_right_border(self.root.right, node.right):
        # if node.right is not None and node.right.data >= self.root.data:
            self.top_view(node.right)

    def is_left_border(self, node, data):
        if node is None:
            return False
        if str(node.data) == str(data):
            return True
        return self.is_left_border(node.left, data)
    
    def is_right_border(self, node, data):
        if node is None:
            return False
        if str(node.data) == str(data):
            return True
        return self.is_right_border(node.right, data)
        
    def special_insert(self, node, dest, data):
        if node.left is not None:
            self.special_insert(node.left, dest, data)
        if str(node.data) == str(dest):
            if node.left is None:
                node.left = Node(data)
            elif node.right is None:
                node.right = Node(data)
            else:
                print("why you insert here!! HUH")
            return
        if node.right is not None:
            self.special_insert(node.right, dest, data)
            
T = BST()
    
inp = [i.split(" ") for i in input("Enter Input : ").split(",")]
T.insert(inp[0][0])
for i in inp:
    T.special_insert(T.root, i[0], i[1])
# T.printTree(T.root)
print("Top view : ", end = "")
T.top_view(T.root)
    