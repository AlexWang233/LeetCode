class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def makeGraph(edges):
            n = len(edges) + 1
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def bfs(graph, maxDist):
            n = len(graph)
            res = [0] * n
            for i in range(n):
                visited = [False] * n
                q = deque()
                q.append((i, 0))
                visited[i] = True
                count = 1
                while q:
                    node, dist = q.popleft()
                    if dist == maxDist:
                        continue
                    for v in graph[node]:
                        if not visited[v]:
                            visited[v] = True
                            q.append((v, dist + 1))
                            count += 1
                res[i] = count
            return res

        g1 = makeGraph(edges1)
        g2 = makeGraph(edges2)

        if k == 0:
            return [1] * len(g1)

        c1 = bfs(g1, k)
        c2 = bfs(g2, k - 1)
        max_c2 = max(c2)

        ans = [c + max_c2 for c in c1]
        return ans