class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        visited = set([])
        dup = -1
        n = len(grid)
        s = set([(i + 1) for i in range(n * n)])
        for row in grid:
            for i in row:
                if dup < 0 and i in visited:
                    dup = i
                visited.add(i)
        
        return [dup] + list(s - visited)