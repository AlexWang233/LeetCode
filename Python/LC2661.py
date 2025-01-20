class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_count, col_count = [0] * n, [0] * m
        d = {}
        for i in range(m):
            for j in range(n):
                d[mat[i][j]] = (i, j)
        for i in range(m * n):
            r, c = d[arr[i]]
            row_count[c] += 1
            col_count[r] += 1
            if row_count[c] == m or col_count[r] == n:
                return i
        return -1
