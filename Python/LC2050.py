class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for i, j in relations:
            graph[i - 1].append(j - 1)

        dp = [-1] * n

        def calcTime(i):
            if dp[i] != -1:
                return dp[i]

            dp[i] = time[i]
            if graph[i]:
                dp[i] += max([calcTime(j) for j in graph[i]])
            return dp[i]

        res = max([calcTime(i) for i in range(n)])

        return res

            



