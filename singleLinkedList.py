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


    
        
ll1 = SingleLinkedList()
ll1.addbegining(1)
ll1.addbegining(2)
ll1.addbegining(3)
ll1.addbegining(4)
ll1.addEnd(4)
ll1.print()
ll1.insert(10,4)
ll1.length()
ll1.insert(10,30)
ll1.print()
ll1.remove(-1)
ll1.print()
ll1.deleteLL()
print('After deletion')
ll1.print()