class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        l = len(grid[0])
        res = 0
        i = 0
        for row in grid:
            i = bisect.bisect(row[::-1], -1, lo = i)
            res += i
        return res