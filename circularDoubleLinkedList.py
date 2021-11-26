class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class CircularDoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print(self):
        if self.head == None:
            print("Empty List")
            return
        tempNode = self.head
        s=str(tempNode.value) + "-->"
        while tempNode.next != self.head:
            tempNode= tempNode.next
            s=s+str(tempNode.value) + "-->"
        print(s)


    def addtoBegin(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
            node.next = node
          
        else:
            lastNode = self.tail
            lastNode.next = node
            node.next = self.head
            self.head = node
            # tempNode = self.head
            # while tempNode.next != self.head:
            #     tempNode= tempNode.next
            # tempNode.next = node
            # node.next = self.head
            # self.head = node

    def addtoEnd(self, value):
        if self.head == None:
            self.addtoBegin(value)
        else:
            node = Node(value)
            lastNode = self.tail
            lastNode.next = node
            node.next = self.head
            node.prev = lastNode
            self.tail = node

    def length(self):
        count = 1
        if self.head == None:
            return 0
        tempNode = self.head
        while tempNode!=self.tail:
            tempNode= tempNode.next
            count +=1
        return count

    def insert(self, value,location):
        if location==0:
            self.addtoBegin(value)
        elif location==-1:
            self.addtoEnd(value)
        else:
            node = Node(value)
            tempNode = self.head
            counter = 0
            while location >= counter+2:
                tempNode=tempNode.next
                counter+=1
            tempNode.next.prev = node
            node.next = tempNode.next
            node.prev = tempNode
            tempNode.next = node

    def deleteFirst(self):
        if self.head == None:
            print("Empty list nothing to delete")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            secondNode = self.head.next
            secondNode.prev = None
            self.head = secondNode
            self.tail.next = secondNode

    def deleteLast(self):
        if self.head == None:
            print("Nothing to delete")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            newLastNode = self.tail.prev
            newLastNode.next = self.head
            self.tail = newLastNode

    def deleteAtLocation(self, location):
        if location > self.length()-1:
            print("Out of bound, nothing to delete")
        elif location==0:
            self.deleteFirst()
        elif location==-1:
            self.deleteLast()
        else:
            counter = 0
            tempNode=self.head
            while location >= counter+2:
                tempNode=tempNode.next
                counter+=1
            nodetoDelete = tempNode.next
            tempNode.next = nodetoDelete.next
            nodetoDelete.next.prev = tempNode

                        
                

cdll= CircularDoubleLinkedList()
cdll.addtoEnd(0)
cdll.print()
cdll.addtoBegin(1)
cdll.print()
cdll.addtoBegin(2)
cdll.print()
cdll.addtoBegin(4)
cdll.print()
cdll.addtoEnd(5)
cdll.print()
cdll.insert(6,3)
cdll.print()
cdll.deleteFirst()
cdll.print()
cdll.deleteLast()
cdll.print()
cdll.deleteAtLocation(2)
cdll.print()
