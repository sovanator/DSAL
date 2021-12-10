class QueueList():
    def __init__(self):
        self.l = []

    def enqueue(self, value):
        self.l.append(value)

    def dequeue(self):
        if self.l is None:
            print("Queue is empty")
            return
        return self.l.pop(0)
    def print(self):
        leng = len(self.l)-1
        s=""
        while leng>=0:
            s = str(self.l[leng]) + "<--" + s
            leng = leng - 1
        print(s)

    def peek(self):
        if self.l is None:
            print("Nothing in queue")
            return
        print(self.l[0])
    def size(self):
        return len(self.l)
# ql = QueueList()
# ql.enqueue(1)
# ql.enqueue(2)
# ql.enqueue(3)
# ql.peek()
# ql.enqueue(4)
# ql.enqueue(5)
# ql.enqueue(6)
# ql.print()
# print(ql.dequeue())
# ql.print()
# print(ql.size())