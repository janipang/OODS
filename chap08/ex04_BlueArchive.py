def key(name):
    return sum([ord(alpha) for alpha in name])

class Node(object):
    def __init__(self, name):
        self.data = name
        self.key = key(name)
        self.left = None
        self.right = None
    
    def getBalance(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return -1 * (self.right.getHeight())
        elif self.right is None:
            return self.left.getHeight()
        return self.left.getHeight() - self.right.getHeight()

    def getHeight(self):
        if self.left is None and self.right is None:
            return 1
        lheight = rheight = 0
        if self.left is not None:
            lheight = self.left.getHeight()
        if self.right is not None:
            rheight = self.right.getHeight()
        if lheight >= rheight:
            return lheight + 1
        else:
            return rheight + 1


class AVL_Tree(object):
    def __init__(self):
        self.root = None

    def getBalance(self, node):
        if node is None:
            return -1
        if node.left is None and node.right is None:
            return 0
        elif node.left is None:
            return -1 * (node.right.getHeight())
        elif node.right is None:
            return node.left.getHeight()
        return node.left.getHeight() - node.right.getHeight()
        
    def insert(self, data):
        self.root = self._insert(self.root, data)
        self.rebalance(self.root)
        
    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if key(data) < root.key:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        return root
    
    def rebalance(self, root):
        if root is None:
            return
        self.rebalance(root.left)
        self.rebalance(root.right)
        if root.getBalance() > 1 and self.getBalance(root.left) >= 1:
            # print("*")
            self.rightRotate(root)
        elif root.getBalance() > 1 and self.getBalance(root.left) <= -1:
            # print("**")
            self.leftRotate(root.left)
            self.rightRotate(root)
        elif root.getBalance() < -1 and self.getBalance(root.right) <= -1:
            # print("***")
            self.leftRotate(root)
        elif root.getBalance() < -1 and self.getBalance(root.right) >= 1:
            # print("****")
            self.rightRotate(root.right)
            self.leftRotate(root)
        
    def delete(self, data):
        self.root = self._delete(self.root, data)
        self.rebalance(self.root)

    def _delete(self, root, data):
        if root is None:
            return root

        if key(data) < root.key:
            root.left = self._delete(root.left, data)
        elif key(data) > root.key:
            root.right = self._delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.find_min_value_node(root.right)
            root.data = temp.data
            root.key = temp.key
            root.right = self._delete(root.right, temp.data)

        return root

    def leftRotate(self, z):
        parent = self.getFather(z)
        y = z.right
        z.right = y.left
        y.left = z
        if parent is None:
            self.root = y
            return
        
        if parent.left == z:
            parent.left = y
        elif parent.right == z:
            parent.right = y

    def rightRotate(self, z):
        parent = self.getFather(z)
        y = z.left
        z.left = y.right
        y.right = z
        if parent is None:
            self.root = y
            return
        
        if parent.left == z:
            parent.left = y
        elif parent.right == z:
            parent.right = y
        # source = https://www.geeksforgeeks.org/insertion-in-an-avl-tree/
    
    def find_min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def getFather(self, node):
        if node == self.root:
            return None
        return self._getFatger(self.root, node)
        
    def _getFatger(self, root, node):
        if root is None:
            return None
        if root.left == node or root.right == node:
            return root
        if self._getFatger(root.left, node) is not None:
            return self._getFatger(root.left, node)
        if self._getFatger(root.right, node) is not None:
            return self._getFatger(root.right, node)
        
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)
    
    def printDirectory(self):
        if self.root is not None:
            self._printDirectory(self.root)
        
    def _printDirectory(self, root, level=0):
        if root is None:
            print(f"{'    ' * level}*")
            return
        print(f"{'    ' * level}{root.data} ({root.key})")
        if root.left is not None or root.right is not None:
            self._printDirectory(root.left, level + 1)
            self._printDirectory(root.right, level + 1)


T = AVL_Tree()
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    if op == "I":
        root = T.insert(data)
    elif op == "D":
        root = T.delete(data)
    elif op == "P":
        T.printDirectory()
        print("------------------------------")