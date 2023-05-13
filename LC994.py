from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        curStack = deque()
        fStack = deque()
        r, c = len(grid), len(grid[0])
        visited = [[False] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    curStack.append((i, j))
                    visited[i][j] = True

        counter = 0
        while curStack or fStack:
            if not curStack:
                curStack = fStack
                fStack = deque()
                counter += 1

            (x, y) = curStack.popleft()
            for a, b in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if a < 0 or b < 0 or a >= r or b >= c:
                    continue
                if visited[a][b]:
                    continue
                visited[a][b] = True
                if grid[a][b] != 1:
                    continue
                grid[a][b] = 2
                fStack.append((a, b))

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return -1

        return counter


