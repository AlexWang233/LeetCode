class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        visited = set([])
        res = set([])
        n = len(grid)
        for row in grid:
            for i in row:
                if i in visited:
                    res.add(i)
                visited.add(i)
        
        s = set([(i + 1) for i in range(n * n)])
        return list(res.union(s - visited))