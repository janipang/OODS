class Node:
    def __init__(self, data,id):
        self.data = data
        self.left = None
        self.right = None
        self.id = id

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
    
    def __str__(self):
        return str(self.data) + ' ' + str(self.id)

class AVL:
    def __init__(self) -> None:
        self.root = None
        self.node_id_counter = 1

    def add(self,data):
        self.root = self._add(self.root,data)
        self.node_id_counter += 1

    def _add(self, root, data):
        if not root:
            return Node(data,self.node_id_counter)

        if data < root.data:
            root.data, data = data, root.data

        if not root.left:
            root.left = self._add(root.left, data)
        elif not root.right:
            root.right = self._add(root.right, data)
        else:
            root.left = self._add(root.left, data)
        return root
        
    def heapify_down(self):
        self._heapify_down(self.root)
        
    def _heapify_down(self, node):
        if not node:
            return

        min = node
        left = node.left
        right = node.right

        if left and (left.data < min.data or (left.data == min.data and left.id < min.id)):
            min = left

        if right and (right.data < min.data or (right.data == min.data and right.id < min.id)):
            min = right

        if min != node:
            node.data, min.data = min.data, node.data
            node.id, min.id = min.id, node.id
            self._heapify_down(min)



    def insertRoot(self,data):
        if self.root is None:
            return
        
        self.root.data += data

    def display(self,customer,time):
        print(f"Customer {customer} Booking Van {self.root.id} | {time} day(s)")

nums,datas = input("Enter Input : ").split("/")

datas = list(map(int,datas.split()))
nums = int(nums)

T = AVL()

for i in range(nums):
    T.add(0)

T.heapify_down()

customer = 1
for data in datas:
    T.insertRoot(data)
    T.display(customer, data)
    customer += 1
    T.heapify_down()