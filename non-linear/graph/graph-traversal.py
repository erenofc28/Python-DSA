class Graph:
    def __init__(self):
        self.graph = {}
        self.visited = []

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, v1, v2, directed=False):
        self.addVertex(v1)
        self.addVertex(v2)
        self.graph[v1].append(v2)
        if not directed:
            self.graph[v2].append(v1)

    def getEdges(self):
        for key, val in self.graph.items():
            for v in val:
                print("(" + key + "," + v + ")")

    def display(self):
        for key in self.graph:
            print(key, '=>', self.graph[key])

    def getVertex(self):
        for key, val in self.graph.items():
            print(key)

    def removeVertex(self, v):
        if v in self.graph:
            del self.graph[v]
        for key, val in self.graph.items():
            if v in val:
                val.remove(v)

    def removeEdge(self, v1, v2):
        if self.isEdge(v1, v2):
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)

    def isEdge(self, v1, v2):
        return v1 in self.graph[v2] or v2 in self.graph[v1]
# DFS
    def dfs(self, start):
        if start not in self.visited:
            self.visited.append(start)
            print(start,end=" ")
        for child in self.graph[start]:
            if child not in self.visited:
                self.dfs(child)
# BFS
    def bfs(self,start):
        queue=[start]
        self.visited=[start]
        while len(queue)>0:
            curr=queue.pop(0)
            for child in self.graph[curr]:
                if child not in self.visited:
                    queue.append(child)
                    self.visited.append(child)
        print(self.visited)
        self.visited = []




g1 = Graph()
g1.addEdge('A', 'B')
g1.addEdge('A', 'C')
g1.addEdge('B', 'D')
g1.addEdge('C', 'D')
g1.addEdge('C','E')
g1.display()
print("bfs")
g1.bfs('A')
print("dfs")
g1.dfs("A")

# print(g1.visited)
