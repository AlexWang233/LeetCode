class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Use quadratic formula from largest x such that x * (x + 1) / 2 <= n
        return int(math.sqrt(8 * n + 1) - 1) // 2