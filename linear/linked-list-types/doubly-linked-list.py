# own code
class node:
    def __init__(self,val=None):
        self.data = val
        self.prev = None
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertBegining(self,val):
        if(self.head is None):
            newnode = node(val)
            self.head = newnode
            self.tail = newnode
            return
        else:
            newnode = node(val)
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode

    def display(self):
        if(not self.head):
            return
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print(" ")
            
    def reverseDisplay(self):
        if (not self.head):
            return
        temp = self.tail
        while temp:
            print(temp.data,end=" ")
            temp = temp.prev
        print(" ")
        return;

    def insertAtPosition(self,pos,val):
        if pos == 0:
            newnode = node(val)
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            return
        newnode = node(val)
        
        curr = self.head
        
        for i in range(0,pos-1):
            curr = curr.next
            
        next = curr.next
    
        curr.next = newnode
        newnode.prev = curr
        
        newnode.next = next
        next.prev = newnode
        
    def deleteAtPosition(self,pos):
        if pos == 0:
            self.head.next.prev = None
            self.head = self.head.next
            
            return
        
        curr = self.head
        for i in range(0,pos-1):
            curr = curr.next
        next = curr.next
        
        curr.next = next.next
        next.next.prev = curr

ll = linkedlist()
ll.insertBegining(10)
ll.insertBegining(20)
ll.insertBegining(30)
ll.insertBegining(40)
print("reversed")
ll.reverseDisplay()
print("normal")
ll.display()
print("adding 31 in 2nd position")
ll.insertAtPosition(2,31)
ll.display()
print("deleting value at 1st position")
ll.deleteAtPosition(0)
ll.display()

#udemy course solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None      
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
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
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp
  



my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before remove():')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() in middle:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() of last node:')
my_doubly_linked_list.print_list()

