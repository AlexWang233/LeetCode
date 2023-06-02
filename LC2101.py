class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n, res, graph = len(bombs), 0, defaultdict(set)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                    graph[i].add(j)

        visited = set()
        def dfs(u):
            nonlocal visited
            for v in graph[u]:
                if v in visited:
                    continue
                visited.add(v)
                dfs(v)

        for i in range(n):
            visited = set([i])
            dfs(i)
            res = max(res, len(visited))

        return res