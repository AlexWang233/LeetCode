class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = 0
        p = n // m
        res += (1 + n) * n // 2
        res -= (1 + p) * p * m
        return res