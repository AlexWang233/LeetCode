class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(lambda: {})
        for i in range(len(values)):
            a = equations[i][0]
            b = equations[i][1]
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]
            graph[a][a] = 1
        for i in graph:
            for j in graph[i]:
                for k in graph[i]:
                    graph[j][k] = graph[j][i] * graph[i][k]

        ans = []
        for a, b in queries:
            if b in graph[a]:
                ans.append(graph[a][b])
            else:
                ans.append(-1)
        return ans