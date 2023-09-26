class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

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
    
    def makeTree(self, n):
        self._makeTree(self.root, n, 1)
        
    def _makeTree(self, node, n, now):
        if now > n:
            return None
        new = Node(ord('c'))
        if self.root is None:
            self.root = new
        new.left = self._makeTree(new, n, 2*now)
        new.right = self._makeTree(new, n, 2*now+1)
        return new
    
    def fillLeaf(self, element):
        Baby = [self.root]
        while len(Baby) != 0:
            node = Baby.pop(0)
            if node.left is None and node.right is None:
                node.data = element.pop(0)
            if node.left is not None:
                Baby.append(node.left) 
            if node.right is not None:
                Baby.append(node.right)
        
    def fill(self, root):
        if root.left is None or root.right is None:
            return
        self.fill(root.left)
        self.fill(root.right)
        root.data = min(root.left.data, root.right.data)
        root.left.data -= root.data
        root.right.data -= root.data
    
    def sumNode(self, root):
        if root is None:
            return 0
        return self.sumNode(root.left) + self.sumNode(root.right) + root.data

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node.data)
            self.print_tree(node.left, level + 1)


text = input("Enter Input : ").split("/")
n, element = int(text[0]), [int(i) for i in text[1].split()]
if len(element) != (n//2) + 1:
    print("Incorrect Input")
    exit(0)
T = BST()
T.makeTree(n)
T.fillLeaf(element)
T.fill(T.root)
# T.print_tree(T.root)
print(T.sumNode(T.root))
