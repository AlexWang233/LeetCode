class Solution:
    def totalNQueens(self, n: int) -> int:
        c = set()
        d = set()
        d2 = set()
        def backtrack(r):
            if row == n:
                return 1
            cnt = 0
            for col in range(n):
                if col in c:
                    continue
                if row - col in d:
                    continue
                if row + col in d2:
                    continue
                c.add(col)
                d.add(row - col)
                d2.add(row + col)
                cnt += backtrack(row + 1)
                c.remove(col)
                d.remove(row - col)
                d2.remove(row + col)
            return cnt
        return backtrack(0)