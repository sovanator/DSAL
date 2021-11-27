class Stack:
    def __init__(self, maxSize):
        self.list = []
        self.maxSize = maxSize
    def isEmpty(self):
        if self.list ==[]:
            return True
        return False

    def isFull(self):
        if len(self.list)==self.maxSize:
            return True
        return False

    def push(self,value):
        if self.isFull():
            print("Stack is full")
            return
        self.list.append(value)
    def isEmpty(self):
        if self.list ==[]:
            return True
        return False

    def pop(self):
        if not self.isEmpty():
            self.list.pop()
        
    def peek(self):
        if not self.isEmpty():
            return self.list[-1]

s = Stack(2)
print(s.isFull())
s.push(1)
s.push(2)
print(s.peek())
print(s.isFull())
s.push(3)