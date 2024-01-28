class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for r in matrix:
            for c in range(n - 1):
                r[c + 1] += r[c]
        res = 0
        for i in range(n):
            for j in range(i, n):
                d = defaultdict(lambda: 0)
                cur = 0
                d[cur] = 1
                for k in range(m):
                    cur += matrix[k][j]
                    if i > 0:
                        cur -= matrix[k][i-1]
                    res += d[cur - target]
                    d[cur] += 1
        return res