# // own code
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

# //udemy course code
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    

    

my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print('Stack before pop():')
my_stack.print_stack()

print('\nPopped node:')
print(my_stack.pop().value)

print('\nStack after pop():')
my_stack.print_stack()


