class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(lambda: set())
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)
        
        ans = 0
        for i in range(n): 
            for j in range(i+1, n):
                val = len(graph[i]) + len(graph[j]) - (j in graph[i])
                ans = max(ans, val)
        return ans 