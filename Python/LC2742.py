class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        l = len(cost)
        # dp[i] represents the minimum cost to paint i walls
        dp = [0] + [math.inf] * l
        for c, t in zip(cost, time):
            for i in range(l, 0, -1):
                prev = max(i - t - 1, 0)
                dp[i] = min(dp[i], dp[prev] + c)
        return dp[-1]
