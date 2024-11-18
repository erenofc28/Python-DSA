class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        newNode = node(value)
        if self.top == None:
            self.top = newNode
            return
        else:
            newNode.next = self.top
            self.top = newNode
    def display(self):
        curr = self.top
        while curr:
            print(curr.val,end = " ")
            curr = curr.next
        print("")
    def peek(self):
        val = self.top.val
        print(val)
    def pop(self):
        if(self.top is None):
            print("stack is empty")
            return
        print(self.top.val,"value popped from stack")
        self.top = self.top.next
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.display()
print("pushing value into stack")
s.push(4)
s.display()
s.pop()
s.display()
print("peek method")
s.peek()
s.peek()
s.peek()
