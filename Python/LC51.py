class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(row):
            # check where to place queen in next row
            if row == n:
                res.append(queens[:])
                return None
            # iterate over all columns to see if it's available
            for col in range(n):
                if col not in queens and row - col not in xy_diff and row + col not in xy_sum:
                    queens.append(col)
                    xy_diff.add(row - col)
                    xy_sum.add(row + col)
                    dfs(row + 1)
                    queens.pop()
                    xy_diff.remove(row - col)
                    xy_sum.remove(row + col)
        res = []
        queens = []
        xy_diff = set()
        xy_sum = set()
        dfs(0)
        boards = []
        for board in res:
            boards.append(["." * i + "Q" + "." * (n - i - 1) for i in board])
        return boards