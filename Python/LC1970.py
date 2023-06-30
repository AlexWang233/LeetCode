class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def existsPath(day):
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            q = deque([])
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
                    grid[0][c] = 1
                    
            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
                for dx, dy in directions:
                    x, y = r + dx, c + dy
                    if x < 0 or x == row or y < 0 or y == col or grid[x][y] == 1:
                        continue
                    grid[x][y] = 1
                    q.append((x, y))
            return False

        left, right = 1, len(cells)
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if existsPath(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res
