class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class StackLL:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        print(self.head)
    def pop(self):
        if self.head == None:
            print("Empty Stack")
        elif self.head.next == None:
            self.head = None
        else:
             self.head = self.head.next
    def peek(self):
         if self.head is not None:
             print(self.head.value)
             return 
         print("Empty Stack")     
    def deleteStack(self):
        if self.head is not None:
            self.head = None
            return
        print("Empty Stack nothing to delete")
    
    def print(self):
        tempNode = self.head
        s = ""
        while tempNode:
            print(tempNode.value)
            s= s +  str(tempNode.value) + "-->"
            tempNode = tempNode.next
        print(s)
            
            
s = StackLL()
s.push(1)
s.push(2)
s.push(3)
s.print()
print(s.head)