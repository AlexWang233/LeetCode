class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = -1
            dfsArr.append((i, j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            
        def first():
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        return i, j

        dfsArr = []
        m, n = len(grid), len(grid[0])
        dfs(*first())
        ans = 0
        while True:
            newArr = []
            while len(dfsArr) > 0:
                x, y = dfsArr.pop()
                for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if i < 0 or j < 0 or i >= m or j >= n:
                        continue
                    if grid[i][j] == 1:
                        return ans
                    elif grid[i][j] == 0:
                        grid[i][j] = -1
                        newArr.append((i, j))
            ans += 1
            dfsArr = newArr

