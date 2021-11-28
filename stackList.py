class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if self.list ==[]:
            return True
        return False
    
    def push(self, value):
        self.list.append(value)
    
    def pop(self):
        if not self.isEmpty():
            self.list.pop()
    def peek(self):
        if not self.isEmpty():
            return self.list[-1]
    def delete(self):
        self.list = []
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
s.pop()
print(s.peek())