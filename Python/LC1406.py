class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * 3
        for i in range(len(stoneValue) - 1, -1, -1):
            n = -10000
            for k in (1, 2, 3):
                n = max(n, sum(stoneValue[i:i+k]) - dp[(i+k) % 3])
            dp[i % 3] = n
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"