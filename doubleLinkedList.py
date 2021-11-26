class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
class dLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def print(self):
        if self.head == None:
            print("Empty List")
        else:
            s= ""
            tempNode = self.head
            while tempNode:
                s=s+str(tempNode.value) + "-->"
                tempNode = tempNode.next
            print(s)
    def length(self):
        l = 0
        if self.head == None:
            return l
        else:
            tempNode = self.head
            while tempNode:
                tempNode=tempNode.next
                l+=1
            return l
    def addbegining(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        
    def addtoEnd(self, value):
        node =Node(value)
        if self.head ==None:
            self.addbegining(value)
        else:
            tempNode = self.head
            while tempNode.next:
                tempNode=tempNode.next
            tempNode.next = node
            node.prev = tempNode
            self.tail = tempNode
    
    def insert(self, value, location):
        if location==0:
            self.addbegining(value)
        elif location ==-1:
            self.addtoEnd(value)
        else:
            node = Node(value)
            if location<=self.length()+1:
                tempNode = self.head
                counter = 0
                while counter<location-1:
                    tempNode=tempNode.next
                    counter+=1
                nextTempNode = tempNode.next
                tempNode.next = node
                node.prev = tempNode
                node.next = nextTempNode
                nextTempNode.prev = node
            else:
                print("Out of linked list")
 
    def deleteFirst(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        secondNode = self.head.next
        self.head = secondNode
        secondNode.prev = None

    def deleteLast(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        tempNode = self.head
        while tempNode.next:
            tempNode=tempNode.next
        secondLastNode = tempNode.prev
        self.tail = secondLastNode
        secondLastNode.next = None

    def deleteAt(self, location):
        if location == -1:
            self.deleteLast()
        elif location == 0:
            self.deleteFirst()
        else:
            if location > self.length():
                print("Nothing to pop")
            else:
                counter = 0
                tempNode = self.head
                while counter <location:
                    counter+=1
                    tempNode = tempNode.next
                tempNode.prev.next = tempNode.next
                tempNode.next.prev = tempNode.prev

    def deleteLL(self):
        self.head = None
        self.tail = None

    def reversePrint(self):
        if self.head==None:
            print("Empty List")
            return
        tempNode = self.tail
        s=str(tempNode.value)+"-->"
        while tempNode.prev:
            s=s+str(tempNode.prev.value) + "-->"
            tempNode=tempNode.prev
        print(s)

    def search(self, value):
        tempNode = self.head
        counter = 0
        while tempNode.value != value:
            tempNode=tempNode.next
            counter+=1
            if tempNode.next == None:
                print("Nada")
                return
        print("Found in location: ", counter)
dll = dLL()
dll.addbegining(1)
dll.addbegining(2)
dll.addtoEnd(3)
dll.insert(4, 0)
dll.insert(5, -1)
# dll.print()
dll.insert(6, 3)
# dll.print()
dll.deleteFirst()
# dll.print()
dll.deleteLast()
dll.print()
dll.deleteAt(6)
dll.print()
# dll.deleteLL()
# dll.print()
dll.reversePrint()
dll.search(8)
# print(dll.length())



        