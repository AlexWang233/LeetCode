class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        arr = [[] for _ in range(n)]
        for start, end, gold in offers:
            arr[end].append([start, gold])
        for end in range(n):
            end += 1
            dp[end] = dp[end - 1]
            for start, gold in arr[end - 1]:
                dp[end] = max(dp[end], dp[start] + gold)
        return dp[-1]