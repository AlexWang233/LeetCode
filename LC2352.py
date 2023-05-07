class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        c = Counter(tuple(row) for row in grid)
        for col in zip(*grid):
            ans += c[col]
        return ans