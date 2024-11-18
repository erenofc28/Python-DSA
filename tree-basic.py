class node:
    def __init__(self,data):
        self.data = data
        self.children = []
class tree:
    def __init__(self):
        self.root = None

    def add(self,parent=0,data=0):
        newnode = node(data)
        if not self.root:
            self.root = newnode
            return
        if parent == self.root.data:
            self.root.children.append(newnode)
            return
        parentFound = self.findParent(parent,self.root)
        if(parentFound):
            parentFound.children.append(newnode)
        else:
            print("parent not found")

    def findParent(self,parent,root):
        if root.data == parent:
            return root
        for child in root.children:
            nodeFound = self.findParent(parent,child)
            if(nodeFound):
                return nodeFound
            print("parent not found (from find parent function)")
        return None
            
            
    def display(self,depth=0,root=None):
        if root:
            print(" " * (depth * 4) + str(root.data))  # Indent by level
        for child in root.children:
            self.display(depth + 1,child)
    
    def remove(self,parent,value):
        parentFound = self.findParent(parent,self.root)
        if not parentFound:
            print("parent not found")
            return
        for child in parentFound.children:
            if child.data == value:
                parentFound.children.remove(child)
                break

t = tree()
t.add(0,10)
t.add(10,20)
t.add(10,30)
t.add(20,21)
print("Tree")
t.display(0,t.root)
print("after removedd 20 from tree")
t.remove(10,20)
t.display(0,t.root)            
