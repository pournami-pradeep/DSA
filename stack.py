class Stack:

    def __init__(self):
        self.stack = []
        self.length = 0
        

    def is_empty(self):
        if self.length == 0:
            return True
        return False
    
    def push(self,data):
        self.stack.append(data)
        self.length = self.length + 1
        self.top = data
        return 
    
    def pop(self):
        if self.is_empty():
            print("Stack is already empty")
            return
        data = self.stack.pop(-1)
        self.length -= 1
        return data
    
    def print_stack(self):
        if self.length == 0:
            print("Stack is empty..")
            return
        for item in self.stack:
            print(f"|{item}|")
     
        return 
    
# stack = Stack()
# stack.push(9)
# stack.push(6)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.pop()
# stack.pop()
# stack.print_stack()
# print(stack.length)



