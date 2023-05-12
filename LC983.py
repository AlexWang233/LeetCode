class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        s = set(days)
        for i in range(1, len(dp)):
            if i not in s:
                dp[i] = dp[i-1]
            else:
                a = dp[max(0, i - 1)] + costs[0]
                b = dp[max(0, i - 7)] + costs[1]
                c = dp[max(0, i - 30)] + costs[2]
                dp[i] = min([a, b, c])
        return dp[-1]

