class Solution:
    def trailingZeroes(self, n: int) -> int:
        cur = 5
        ans = 0
        while cur <= n:
            ans += n // cur
            cur *= 5
        return ans