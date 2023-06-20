from heapq import heappush, heappop

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        r, c = len(grid), len(grid[0])
        if grid[r-1][c-1] == 1:
            return -1

        visited = set()
        prevNode = dict()
        distance = {(0, 0): 0}
        q = []
        heappush(q, (0, (0, 0)))

        def getSuccessors(node):
            x, y = node
            successors = []
            for i in (1, 0, -1):
                for j in (1, 0, -1):
                    if i == 0 and j == 0:
                        continue
                    a, b = x + i, y + j
                    if a < 0 or b < 0 or a >= r or b >= c:
                        continue
                    if grid[a][b] == 1:
                        continue
                    successors.append((a, b))
            return successors

        while q:
            p, node = heappop(q)
            if node in visited:
                continue
            if node == (r-1, c-1):
                ans = 1
                n = node
                while n != (0, 0):
                    n = prevNode[n]
                    ans += 1
                return ans
            visited.add(node)
            for successor in getSuccessors(node):
                x, y = successor
                d = distance[node] + 1
                priority = d + max(abs(r - 1 - x), abs(c - 1 - y))
                heappush(q, (priority, successor))
                if successor not in distance or d < distance[successor]:
                    distance[successor] = d
                    prevNode[successor] = node
                    
        return -1
        