class CircularQ:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.item = [None]*maxSize
        self.head = -1
        self.tail =  -1

    def isFull(self):
        if self.tail + 1 == self.head:
            return True
        elif self.head == 0 and self.tail == self.maxSize:
            return True
        return False
    
    def isEmpty(self):
        if self.tail == -1:
            return True
        return False

    def enqueue(self, value):
        if self.isFull:
            print("Full can't add")
        