class Node:
    def __init__(self, value=None):
        self.value =value
        self.next = None
    
class CircularLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        tempNode = self.head
        print('here', tempNode.value)
        s=""
        if self.head == None:
            print('Empty list')
        elif self.head == self.head.next:
            print("single node ",self.head.value)
        else:
            while tempNode.next !=self.head:
                # print("tempNode.value ", tempNode.value)
                s=s+ str(tempNode.value) + "-->"
                tempNode=tempNode.next
            s=s+str(self.tail.value)
            print(s)
    def createCSLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
    def addtoBegining(self, value):
        if self.head is None:
            print('New list created')
            self.createCSLL(value)
        else:
            node = Node(value)
            # print("value = ", value)
            tempNode = self.head
            # print("tempNode ", tempNode.value)
            while tempNode.next != self.head:
                tempNode=tempNode.next
            node.next = self.head
            self.head = node
            tempNode.next = node
    def addtoEnd(self,value):
        if self.head == None:
            self.createCSLL(value)
        else:
            node=Node(value)
            tempNode = self.head
            while tempNode.next !=self.head:
                tempNode = tempNode.next
            tempNode.next = node                    
            node.next = self.head
            self.tail = node
    def length(self):
        tempNode = self.head
        l =0
        while tempNode.next != self.head:
            tempNode = tempNode.next
            l = l+1
        return l
    def addLocation(self, value, location):
        if location > self.length()+2:
            print('Out of bound')
        elif location == 0:
            self.addtoBegining(value)
        elif location == -1:
            self.addtoEnd(value)
        else:
            node = Node(value)
            tempNode = self.head
            count = 0
            while count < location-1:
                count+=1
                tempNode=tempNode.next
            node.next = tempNode.next
            tempNode.next = node
ll1= CircularLinkedList()
# ll1.createCSLL(2)
ll1.createCSLL(1)
# print(ll1.head.value)
ll1.addtoBegining(2)
ll1.addtoBegining(3)
ll1.addtoBegining(4)
ll1.addtoEnd(20)
ll1.print()
print(ll1.length())
ll1.addLocation(30, -1)
ll1.print()