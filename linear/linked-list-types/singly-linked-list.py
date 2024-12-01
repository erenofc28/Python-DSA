# // my own code
class node:
    def __init__(self,val):
        self.val = val
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,val):
    
        if self.head is None:
            newnode = node(val)
            self.head = newnode
            return
        else:
            newnode = node(val)
            newnode.next = self.head
            self.head = newnode
            return
    def display(self):
        curr = self.head
        while curr:
            print(curr.val,end= " ")
            curr = curr.next
        print("")
        return
    def insertAtPosition(self,pos,val):
        curr = self.head
        newnode = node(val)
        if(pos==0):
            newnode.next = self.head
            self.head = newnode
            return
        else:
            for i in range(0,pos-1):
                curr = curr.next
        next = curr.next
        curr.next = newnode
        newnode.next = next
    def deleteAtPosition(self,pos):
        if pos == 0:
            self.head = self.head.next
            return
        curr = self.head
        for i in range(0,pos-1):
            curr = curr.next
        curr.next = curr.next.next
ll = linkedlist()
ll.insertAtBeginning(5)
ll.insertAtBeginning(4)
ll.insertAtBeginning(3)
ll.insertAtBeginning(2)
ll.insertAtBeginning(1)
print("display linkedlist")
ll.display()
print("inserting 1.1 at 1st position")
ll.insertAtPosition(1,1.1)
ll.display()
print("deleting value at postion at 2nd postion")
ll.deleteAtPosition(2)
ll.display()

# // udemy course solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
  



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()

my_linked_list.reverse()

print('\nLL after reverse():')
my_linked_list.print_list()


