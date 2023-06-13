class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = {}
        l = len(s1)

        for i in range(l):
            if s1[i] not in graph:
                graph[s1[i]] = set()
            if s2[i] not in graph:
                graph[s2[i]] = set()
            graph[s1[i]].add(s2[i])
            graph[s2[i]].add(s1[i])

        for key in graph.keys():
            graph[key].add(key)
            graph[key] = sorted(list(graph[key]))
        
        visited = set()
        def dfs(c):
            if c in visited:
                return c
            visited.add(c)
            ans = c
            if c not in graph:
                return ans
            for d in graph[c]:
                ans = min(ans, dfs(d))
            return ans
        
        res = ""
        for c in baseStr:
            res += dfs(c)
            visited = set()

        return res