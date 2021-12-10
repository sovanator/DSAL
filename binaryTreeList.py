from queueList import QueueList


class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None


    
class ListBT():
    def __init__(self, treeSize):
        self.tree_list= [None]*(treeSize+1)
        self.treeSize = treeSize

    def addNode(self, value):
        iterator = 1
        while True and iterator<self.treeSize+1:
            if self.tree_list[iterator]==None:
                node = Node(value)
                self.tree_list[iterator]= node 
                node.left = 2*iterator
                node.right = 2*iterator + 1
                break
            iterator+=1
        if iterator > self.treeSize:
            print("Out of bound")

    def preOrder(self, rootNode=None):
        if rootNode is None:
            rootNode = self.tree_list[1]
        if rootNode:
            print(rootNode.value)
            if rootNode.left <= self.treeSize:
                self.preOrder(self.tree_list[rootNode.left])
            if rootNode.right <= self.treeSize:
                self.preOrder(self.tree_list[rootNode.right])
        return
    
    def postOrder(self, rootNode=None):

    

        if rootNode is None:
            rootNode = self.tree_list[1]
        if rootNode:
            if rootNode.left <= self.treeSize:
                self.postOrder(self.tree_list[rootNode.left])
            if rootNode.right <= self.treeSize:
                self.postOrder(self.tree_list[rootNode.right])
            print(rootNode.value)
        return
    
    def inOrder(self, rootNode=None):
        if rootNode is None:
            rootNode = self.tree_list[1]
        if rootNode:
            if rootNode.left <= self.treeSize:
                self.inOrder(self.tree_list[rootNode.left])
            print(rootNode.value)
            if rootNode.right <= self.treeSize:
                self.inOrder(self.tree_list[rootNode.right])
        return

    def levelOrder(self):
        q = QueueList()
        level_list =[]
        rootNode = self.tree_list[1]
        q.enqueue(rootNode)
        while q.size()>0:
            rootNode = q.dequeue()
            level_list.append(rootNode.value)
            if rootNode.left <=self.treeSize:
                q.enqueue(self.tree_list[rootNode.left])
            if rootNode.right <=  self.treeSize:
                q.enqueue(self.tree_list[rootNode.right])
        print(level_list)

    def print(self):
        for item in self.tree_list:
            if item is not None:
                print(item.value)
            else:
                print(item)
    def size(self):
        print(len(self.tree_list))

    def searchNode(self, value):
        rootNode  = self.tree_list[1]
        q = QueueList()
        q.enqueue(rootNode)
        while q.size()>0:
            rootNode = q.dequeue()
            if str(rootNode.value) == str(value):
                return True
            if rootNode.left<=self.treeSize:
                q.enqueue(self.tree_list[rootNode.left])
            if rootNode.right<=self.treeSize:
                q.enqueue(self.tree_list[rootNode.right])
        return False   

    def deleteNode(self, value):
        if not self.isEmpty():
            rootNode = self.tree_list[1]
            q = QueueList()
            q.enqueue(rootNode)
            while q.size()>0:
                compareNode = q.dequeue()
                search = False
                print(compareNode)
                input("")
                print(compareNode.value)
                input("")
                if str(compareNode.value) == str(value):
                    search = True
                    break
                if compareNode.left<=self.treeSize:
                    q.enqueue(self.tree_list[compareNode.left])
                if compareNode.right<=self.treeSize:
                    q.enqueue(self.tree_list[compareNode.right])
            if search is True:
                for item in self.tree_list[::-1]:
                    if item is not None:
                        compareNode.value = item.value
                        print("___________")
                        print(compareNode)
                        print(compareNode.value)
                        print(compareNode.left)
                        print(compareNode.right)
                        input("")
                        self.tree_list.remove(item)
                        return True
            return False
        return "Nothing to delete Empty Tree"
    def isEmpty(self):
        return not self.tree_list[1]
bt = ListBT(4)
bt.addNode("A")
bt.addNode("b")
# bt.addNode("c")
# bt.addNode("d")
# bt.addNode(5)
# bt.print()
# bt.size()
# bt.inOrder()
# print(bt.searchNode("d"))
# bt.print()
bt.deleteNode("A")
bt.deleteNode("B")
bt.print()
# bt.levelOrder()
