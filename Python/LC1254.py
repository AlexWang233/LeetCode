class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        islandNum = 0
        visited = [[False] * c for i in range(r)]
        
        def closeIsland(i: int, j: int) -> bool:
            
            if i < 0 or j < 0 or i >= r or j >= c:
                return False
            
            if grid[i][j] == 1 or visited[i][j]:
                return True
            
            visited[i][j] = True
            
            top = closeIsland(i - 1, j)
            bottom = closeIsland(i + 1, j)
            left = closeIsland(i, j - 1)
            right = closeIsland(i, j + 1)
            
            return top and bottom and left and right
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0 and visited[i][j] == False:
                    if closeIsland(i, j):
                        islandNum += 1
        
        return islandNum