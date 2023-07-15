print("* Stack Calculator *")

class Stack():
	def __init__(self):
		self.stack = []
	
	def is_empty(self):
		if len(self.stack) <= 0:
			return 1
		return 0

	def push(self, obj):
		self.stack.append(obj)
	
	def pop(self):
		if self.is_empty():
			print(-1)
			return
		return self.stack.pop()
	
	def peek(self):
		if len(self.stack) == 0:
			return None
		return self.stack[-1]
	
	def __len__(self):
		return len(self.stack)
	
	def __str__(self):
		return str(self.stack)

class Calculator:
    def __init__(self):
        self.instructions = ["+", "-", "*", "/", "DUP", "POP", "PSH"]
        self.val_to_calc = Stack()
        # self.do_list = [self.add(), self.subtract(), self.multiply(), self.divide(), self.DUP(), self.POP(), self.PSH()]
    
    def add(self):
        self.val_to_calc.push(self.val_to_calc.pop() + self.val_to_calc.pop())
    
    def subtract(self):
        self.val_to_calc.push(self.val_to_calc.pop() - self.val_to_calc.pop())
        
    def multiply(self):
        self.val_to_calc.push(self.val_to_calc.pop() * self.val_to_calc.pop())
        
    def divide(self):
        self.val_to_calc.push(self.val_to_calc.pop() / self.val_to_calc.pop())
        
    def DUP(self):
        self.val_to_calc.push(self.val_to_calc.peek())
        
    def POP(self):
        return self.val_to_calc.pop()
    
    def PSH(self):
        pass
    
    def run(self, cmd):
        for ele in cmd:
            if ele in self.instructions:
                # self.do_list[self.instructions.index(ele)]
                if ele == '+': self.add()
                elif ele == '-': self.subtract()
                elif ele == '*': self.multiply()
                elif ele == '/': self.divide()
                elif ele == "DUP": self.DUP()
                elif ele == "POP": self.POP()
                elif ele == "PSH": self.PSH()
            else:
                try:
                    self.val_to_calc.push(int(ele))
                except ValueError:
                    print("Invalid instruction: " + ele)
                    exit()
        if self.val_to_calc.is_empty():
            print(0)
        else:
        	print(int(self.val_to_calc.peek()))
        
                

rfx94 = Calculator()
command = list(map(str, input("Enter arguments : ").split(' ')))
rfx94.run(command)