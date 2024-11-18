class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,val):
        newnode = node(val)
        if(self.front == None):
            self.front = newnode
            self.rear = newnode
            return
        else:
            self.rear.next = newnode
            self.rear = newnode

    def dequeue(self):
        if(self.front is None):
            print("queue is empty")
            return
        print(self.front.val,"removed from queue")
        self.front = self.front.next
    def peek(self):
        if(self.front is None):
            print("queue is empty")
            return
        print(self.front.val,"peek value")
    def display(self):
        if (self.front is None):
            print("queue is empty")
            return
        curr = self.front
        while curr:
            print(curr.val,end=" ")
            curr = curr.next
        print("")
q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print("4 added into queue")
q.enqueue(4)
q.display()
print("dequeue method")
q.dequeue()
q.display()
print("peek method")
q.peek()
q.peek()
