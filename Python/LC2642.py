class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for a, b, cost in edges:
            self.graph[a].append((b, cost))

    def addEdge(self, edge: List[int]) -> None:
        a, b, cost = edge
        self.graph[a].append((b, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.graph)
        pq = [(0, node1)]
        dist = [inf] * n
        dist[node1] = 0

        while pq:
            d, node = heappop(pq)
            if node == node2:
                return d
            if d > dist[node]:
                continue
            for ngbr, cost in self.graph[node]:
                nd = d + cost
                if nd < dist[ngbr]:
                    dist[ngbr] = nd
                    heappush(pq, (nd, ngbr))

        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)