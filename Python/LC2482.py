class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        row = [0] * r
        col = [0] * c
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
                else:
                    row[i] -= 1
                    col[j] -= 1

        for i in range(r):
            for j in range(c):
                grid[i][j] = row[i] + col[j]

        return grid