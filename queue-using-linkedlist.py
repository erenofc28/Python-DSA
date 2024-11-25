//own code
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

//udemy course code
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue().value)
# (1) Item -  Returns 1 Node
print(my_queue.dequeue().value)
# (0) Items - Returns None
print(my_queue.dequeue())


