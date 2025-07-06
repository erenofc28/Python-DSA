    def bfs(self, adj):
        # code here
        from collections import deque
        q = deque()
        q.append(0)
        visited = set()
        res = []
        graph = {}
        for i in range(len(adj)):
            graph[i] = adj[i]
        
        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            res.append(node)
            for child in graph[node]:
                if child not in visited:
                    q.append(child)
        return res
