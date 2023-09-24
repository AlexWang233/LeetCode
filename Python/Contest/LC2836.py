class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        m = (k+1).bit_length()
        jump = [[0]*n for i in range(m)]
        val = [[0]*n for i in range(m)]
        jump[0] = receiver
        val[0] = list(range(n))
        for i in range(1, m):
            for j in range(n):
                jump[i][j] = jump[i-1][jump[i-1][j]]
                val[i][j] = val[i-1][j] + val[i-1][jump[i-1][j]]
        res = 0
        for i in range(n):
            cur = 0
            pos = i
            for j in range(m):
                if (k+1) & (1<<j):
                    cur += val[j][pos]
                    pos = jump[j][pos]
            res = max(res, cur)
        return res