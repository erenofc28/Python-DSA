class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class binaryTree:
    def __init__(self):
        self.root = None

    def add(self,data):
        if not self.root:
            self.root = node(data)
            return
        self.recursiveAdd(data,self.root)

    def recursiveAdd(self,data,root):
        if not root:
            root = node(data)
            return
        elif not root.left:
            root.left = node(data)
            return
        elif not root.right:
            root.right = node(data)
            return
        else:
            self.recursiveAdd(data,root.left)

    def display(self,depth,root):
        if not root:
            return
        print(" "*depth,root.data)
        if (root.left):
            self.display(depth+1,root.left)
        if root.right:
            self.display(depth+1,root.right)

    def remove(self,data):
        if self.root.data == data:
            self.root = None
            return
        self.recursiveRemove(data,self.root)

    def recursiveRemove(self,data,root):
        if root is None:
            return
       
        if root.data == data:
            print(root.data,'in')
            root = None
            return
        if root.left and root.left.data == data:
            root.left = None
        if root.right and root.right.data == data:
            root.right = None
        if root.left:
            self.recursiveRemove(data,root.left)
        if root.right:
            self.recursiveRemove(data,root.right)


    def search(self,data):
        self.found = False
        self.searchRecursive(data,self.root)
        if(self.found):
            print(data,"successfuly found")
        else:
            print(data,"not found")

    def searchRecursive(self,data,root):
        if root.data == data:
            self.found = True
            return
        if root.left:
            self.searchRecursive(data,root.left)
        if root.right:
            self.searchRecursive(data,root.right)
        

bt = binaryTree()
bt.add(10)
bt.add(20)
bt.add(30)
bt.add(40)
bt.display(0,bt.root)
print("after removed 30")
bt.remove(30)
bt.display(0,bt.root)
print("search method (input -> 40)")
bt.search(40)
