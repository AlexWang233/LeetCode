class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dfs = deque([])
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dfs.append((i, j))
        
        dist = [[-1] * n for _ in range(n)]

        depth = 0
        ngbr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while len(dfs) > 0:
            cur = deque([])
            while len(dfs) > 0:
                r, c = dfs.pop()
                if dist[r][c] > -1:
                    continue
                dist[r][c] = depth
                for dx, dy in ngbr:
                    x, y = r + dx, c + dy
                    if 0 <= x < n and 0 <= y < n:
                        cur.append((x, y))
            dfs = cur
            depth += 1
        
        pq = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        while pq:
            d, r, c = heapq.heappop(pq)
            if visited[r][c]:
                continue
            visited[r][c] = True
            if r == c == n - 1:
                return -d            
            for dx, dy in ngbr:
                x, y = r + dx, c + dy
                if 0 <= x < n and 0 <= y < n:
                    heapq.heappush(pq, (max(d, -dist[x][y]), x, y))
        return -1
                
        
            