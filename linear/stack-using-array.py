class stack:
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def peek(self):
        val = self.stack.pop()
        self.stack.append(val)
        print(val)

    def display(self):
        for i in self.stack:
            print(i,end=" ")
        print("")

s = stack()
s.push(1)
s.push(2)
s.push(3)
s.display()
print("pushing value into stack")
s.push(4)
s.display()
print("value popped from stack")
s.pop()
s.display()
print("peek method")
s.peek()
s.display()
