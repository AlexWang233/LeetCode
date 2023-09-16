class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])
        table = [[10000000] * c for _ in range(r)]
        directions = ((0, 1), (-1, 0), (1, 0), (0, -1))
        hp = [(0, 0, 0)]
        
        while hp:
            prev, x, y = heappop(hp)
            if x == r - 1 and y == c - 1:
                return prev
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < r and 0 <= ny < c:
                    cur = max(prev, abs(heights[x][y] - heights[nx][ny]))
                    if cur < table[nx][ny]:
                        table[nx][ny] = cur
                        heappush(hp, (cur, nx, ny))

        return -1