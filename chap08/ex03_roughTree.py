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
    
    def makeTree(self, n, next):
        if next > n:
            return
        self.makeTree(n, next+1)
        self.makeTree(n, next+2)
        self.insert(n, next+1)
        
    def fill(self, root):
        self.fill(root.left)
        self.fill(root.right)
        if self.left or self.right is None:
            return
        root.data = min(root.left.data, root.right.data)
        root.left.data -= root.data
        root.right.data -= root.data

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        if root is None:
            print("Error! Not Found DATA")
            return root

        if data < root.data:
            root.left = self._delete(root.left, data)
        elif data > root.data:
            root.right = self._delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.find_min_value_node(root.right)
            root.data = temp.data
            root.right = self._delete(root.right, temp.data)

        return root

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
for i in element:
    T.insert(i)
T.print_tree(T.root)
