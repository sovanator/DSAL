class Node:
    def __init__(self, value=None):
        self.value= value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def addbegining(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    def addEnd(self,value):
        newNode = Node(value)
        if self.head is None:
            self.addbegining(newNode)
        else:
            tempNode = self.head
            while tempNode.next:
                tempNode=tempNode.next
            tempNode.next = newNode
    def length(self):
        tempNode = self.head
        count=1
        while tempNode.next:
            tempNode = tempNode.next
            count+=1
        return count

    def insert(self, value, location):
        print('this is self', self.length())
        if self.length() + 1 < int(location):
            print("Lenght of the list is", self.length())
        else:
            newNode = Node(value)
            count = 0
            tempNode = self.head
            while count<location-1:
                count+=1
                tempNode=tempNode.next
            newNode.next = tempNode.next
            tempNode.next = newNode

    def print(self):
        iterNode = self.head
        s=""
        while iterNode:
            s+= str(iterNode.value) + '-->'
            iterNode= iterNode.next
            
        print(s)

    def remove(self, location):
        if self.length()<location:
            print("No location found")
        if location==0:
            self.head = self.head.next
        elif location==-1:
            tempNode = self.head
            counter=0
            while self.length()-2>counter:
                tempNode=tempNode.next
                counter+=1
            tempNode.next = None

        else:
            count = 0
            tempNode = self.head
            while count<location -1:
                count +=1
                tempNode = tempNode.next
            tempNode.next = tempNode.next.next
    def deleteLL(self):
        self.head = None
    def removeDup(self):
        s = set()
        location = 0
        tempNode = self.head
        while tempNode:
            if tempNode.value in s:
                self.remove(location)
            else:
                location+=1
            s.add(tempNode.value)
            tempNode=tempNode.next
        print(s)



ll = SingleLinkedList()    
        
ll.addbegining(1)
ll.addbegining(2)
ll.addbegining(3)
ll.addbegining(4)
ll.addbegining(5)
ll.addbegining(6)
ll.addbegining(1)
ll.addbegining(2)
ll.addbegining(3)
ll.addbegining(4)
ll.addbegining(5)
ll.print()
ll.removeDup()
ll.print()
