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
