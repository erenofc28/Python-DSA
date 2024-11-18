class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.append(val)

    def dequeue(self):
        print(self.queue.pop(0),"removed from queue")
    
    def peek(self):
        if(len(self.queue)==0):
            print("queue is empty")
            return
        print(self.queue[0])
    def display(self):
        for i in self.queue:
            print(i,end=" ")
        print("")

q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print("value added into queue")
q.enqueue(4)
q.display()
q.dequeue()
q.display()
print("peek method")
q.peek()
q.peek()
