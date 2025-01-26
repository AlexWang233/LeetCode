class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque([])
        n, m = len(isWater), len(isWater[0])
        ans = [[m * n] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    ans[i][j] = 0
        depth = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            depth += 1
            temp = deque([])
            for x, y in q:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if ans[nx][ny] > depth:
                        temp.append((nx, ny))
                        ans[nx][ny] = depth
            q = temp
        return ans



                