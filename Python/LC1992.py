class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def survey(i, j):
            while i < r - 1 and land[i + 1][j]:
                i += 1
            while j < c - 1 and land[i][j + 1]:
                j += 1
            return (i, j)
        r, c = len(land), len(land[0])
        res = []
        for i in range(r):
            for j in range(c):
                if land[i][j]:
                    if i > 0 and land[i-1][j]:
                        continue
                    if j > 0 and land[i][j-1]:
                        continue
                    p, q = survey(i, j)
                    res.append([i, j, p, q])
        return res

