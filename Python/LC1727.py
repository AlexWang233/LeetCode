class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        for j in range(n):
            for i in range(1, m):
                matrix[i][j] += matrix[i-1][j] if matrix[i][j] else 0

        for i in range(m):
            matrix[i].sort(reverse = True)
            for j in range(n):
                res = max(res, (j + 1) * matrix[i][j])

        return res