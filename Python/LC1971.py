class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(lambda: set())
        visited = defaultdict(lambda: False)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        q = deque([source])
        visited[source] = True
        while q:
            u = q.pop()
            if u == destination:
                return True
            for v in graph[u]:
                if visited[v]:
                    continue
                visited[v] = True
                q.append(v)
        return False
