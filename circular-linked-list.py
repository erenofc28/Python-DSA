class node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
class linkedlist:
    def __init__(self):
        self.last = None
    
    def insertAtBeginning(self,val):
        newnode = node(val)
        if(self.last is None):
            self.last = newnode
            newnode.next = self.last
            return
        else:
            newnode.next = self.last.next
            self.last.next = newnode

    def insertAtEnd(self,val):
        newnode = node(val)
        if(self.last is None):
            self.last = newnode
            newnode.next = self.last
            return
        newnode.next = self.last.next
        self.last.next = newnode
        self.last = newnode
    def display(self):
        curr = self.last.next
        while True:
            #do
            print(curr.val,end = " ")
            curr = curr.next
            #stop condition
            if curr == self.last.next:
                break
        print("")
    def deleteAtBeginning(self):
        if self.last is None:
            return
        if self.last.next == self.last:
            self.last = None
            return
        self.last.next = self.last.next.next
    def deleteAtEnd(self):
        if self.last is None:
            return
        if self.last.next == self.last:
            self.last = None
            return
        curr = self.last.next
        while curr.next != self.last:
            curr = curr.next
        curr.next = self.last.next
        self.last = curr

ll = linkedlist()
ll.insertAtBeginning(5)
ll.insertAtBeginning(4)
ll.insertAtBeginning(3)
print("linked list")
ll.display()
print("after inserting value at the beginning of linkedlist")
ll.insertAtBeginning(2)
ll.display()
print("after inserting value at the end of linkedlist")
ll.insertAtEnd(10)
ll.display()
ll.deleteAtBeginning()
print("after deleting value at the beginning")
ll.display()
print("after deleting value at the end")
ll.deleteAtEnd()
ll.display()
