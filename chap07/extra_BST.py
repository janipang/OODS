operator = ['+', '-', '*', '/']
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

    def find_min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node.data)
            self.print_tree(node.left, level + 1)

    def printinfix(self, node, output = ''):
        if node != None:
            if node.data in operator:
                output += str("(")
            output = self.printinfix(node.left, output)
            output += str(node.data)
            output = self.printinfix(node.right, output)
            if node.data in operator:
                output += str(")")
        return output
    
    def printprefix(self, node, output = ''):
        if node != None:
            output += str(node.data)
            output = self.printprefix(node.left, output)
            output = self.printprefix(node.right, output)
        return output
        
class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self) -> str:
        s = "Stack of " + str(self.size()) + " items :"
        for ele in self.items:
            s += str(ele)+''
        return s
    
    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
def Infix_to_Profix(str_input:str):
    operator_list = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    s = Stack()
    output = ""
    for i in str_input:
        if i.isalnum():
            output += i
        elif i == '(':
            s.push(i)
        elif i == ')':
            while s.size() != 0 and s.peek() != '(':
                next_op = s.pop()
                output += next_op
            s.pop()
        elif i in operator_list:
            while (s.size() != 0 and s.peek() != '(' and operator_list[i] <= operator_list[s.peek()]):
                next_op = s.pop()
                output += next_op
            s.push(i)

    while not s.isEmpty():
        output += s.pop()
 
    return output

# ทำ  post to infix ก่อน
# ทำ infix to prefix
# ทำ prefix to tree


tree = BST()
stack = Stack()
operator = ['+', '-', '*', '/']
input_value = input("Enter Postfix : ")
for i in input_value:
    if i not in operator :
        stack.push(Node(i))
    else :
        a = stack.pop()
        b = stack.pop()
        c = Node(i, b, a)
        stack.push(c)
print("Tree :")
a = stack.pop()
tree.print_tree(a)
print("--------------------------------------------------")
print(f"Infix : {tree.printinfix(a)}")
print(f"Prefix : {tree.printprefix(a)}")


# tree to infix


