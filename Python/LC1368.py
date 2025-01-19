from collections import deque 

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dq = deque([(0, 0)])
        dist[0][0] = 0
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        while dq:
            x, y = dq.popleft()
            curDir = grid[x][y] - 1
            for i in range(4):
                x2, y2 = x + dx[i], y + dy[i]
                if 0 <= x2 < m and 0 <= y2 < n:
                    cost = dist[x][y] + (0 if i == curDir else 1)
                    if cost < dist[x2][y2]:
                        dist[x2][y2] = cost
                        if i == curDir:
                            dq.appendleft((x2, y2))
                        else:
                            dq.append((x2, y2))
        return dist[m-1][n-1]