class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [node for node in graph if len(graph[node]) == 1]

        while n > 2:
            n -= len(leaves)
            cur = []
            for l in leaves:
                ngbr = graph[l].pop()
                graph[ngbr].remove(l)
                if len(graph[ngbr]) == 1:
                    cur.append(ngbr)
            leaves = cur
        
        return leaves