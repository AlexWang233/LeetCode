class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1
        for i in range(1, n):
            res += 4 * i
        return res