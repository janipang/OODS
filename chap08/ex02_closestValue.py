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
            
    def closestValue(self, value):
        return self._closestValue(self.root, value, self.root) #เพื่อความเป็นสิริมงคล
        
    def _closestValue(self, root, data, closest):
        if root is None:
            return closest
        # ส่งซ้าย
        if abs(root.data - data) <= abs(closest.data - data):
            closest = self._closestValue(root.left, data, root)
        else:
            closest = self._closestValue(root.left, data, closest)
        # ส่งขวา
        if abs(root.data - data) <= abs(closest.data - data):
            closest = self._closestValue(root.right, data, root)
        else:
            closest = self._closestValue(root.right, data, closest)
        return closest
    
T = BST()
text = input("Enter Input : ").split("/")
element, value = text[0], int(text[1])
inp = [int(i) for i in element.split()]
for i in inp:
    root = T.insert(i)
    T.printTree(T.root)
    print("--------------------------------------------------")
print(f"Closest value of {value} : {T.closestValue(value)}")