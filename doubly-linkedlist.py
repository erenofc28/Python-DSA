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
