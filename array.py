class arr:
    def __init__(self):
        self.arr = []
    def insertAtEnd(self,val):
        self.arr.append(val)
        
    def insertAtPosition(self,pos,val):
        self.arr.insert(pos,val)
        
    def deleteAtEnd(self):
        self.arr.pop()
        
    def deleteAtPosition(self,pos):
        self.arr.pop(pos)

    def display(self):
        print("array => ",end="")
        for i in self.arr:
            print(i,end = " ")
        print("")
arr = arr()
while True:
    
    print("1) insertAtEnd")
    print("2) insertAtPosition")
    print("3) deleteAtEnd")
    print("4) deleteAtPosition")
    print("5) display")
    choice = int(input("enter your choice "))
  
    if(choice == 1):
        value = int(input("enter value "))
        arr.insertAtEnd(value)
    elif(choice == 2):
        value = int(input("enter value "))
        pos = int(input("enter position "))
        arr.insertAtPosition(pos,value)
    elif(choice == 3):
        arr.deleteAtEnd()
    elif(choice == 4):
        pos = int(input("enter position "))
        arr.deleteAtPosition(pos)
    elif(choice == 5):
        arr.display()
