class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [10001] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i >= c else 10000 for c in coins]) + 1

        return dp[-1] if dp[-1] <= 10000 else -1