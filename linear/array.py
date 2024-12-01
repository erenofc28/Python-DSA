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

#basic array methods
#  Append: Adds an element to the end of the array.

# python
arr = [1, 2, 3]
arr.append(4)
print(arr)  # Output: [1, 2, 3, 4]
# Insert: Inserts an element at a specified position.

# python
arr = [1, 2, 3]
arr.insert(1, 4)
print(arr)  # Output: [1, 4, 2, 3]
# Remove: Removes the first occurrence of a specified element.

# python
arr = [1, 2, 3, 2]
arr.remove(2)
print(arr)  # Output: [1, 3, 2]
# Pop: Removes and returns the element at a specified position (default is the last element).

# python
arr = [1, 2, 3]
arr.pop()
print(arr)  # Output: [1, 2]
arr.pop(0)
print(arr)  # Output: [2]
# Index: Returns the index of the first occurrence of a specified element.

# python
arr = [1, 2, 3]
print(arr.index(2))  # Output: 1
# Count: Returns the number of occurrences of a specified element.

# python
arr = [1, 2, 3, 2]
print(arr.count(2))  # Output: 2
# Sort: Sorts the array in ascending order.

# python
arr = [3, 1, 2]
arr.sort()
print(arr)  # Output: [1, 2, 3]
# Reverse: Reverses the order of the array.

# python
arr = [1, 2, 3]
arr.reverse()
print(arr)  # Output: [3, 2, 1]
# Extend: Adds all elements of an iterable (like another list) to the end of the array.

# python
arr = [1, 2, 3]
arr.extend([4, 5])
print(arr)  # Output: [1, 2, 3, 4, 5]
# These methods are fundamental for manipulating arrays (or lists) in Python and are frequently used in various data structures and algorithms       
