    def dfs(self, adj):
        # code here
        graph = {}
        for i in range(len(adj)):
            graph[i] = adj[i]
        res = []
        visited = set()
        stack = [0]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            res.append(node)
            visited.add(node)
            for child in graph[node][::-1]:
                if child not in visited:
                    stack.append(child)
        return res
