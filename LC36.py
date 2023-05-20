class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        p = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                q = "[" + board[i][j] + "]"
                qs = set((str(i) + q, q + str(j), str(i//3) + q + str(j//3)))
                if qs & p: return False
                p = p | qs
        return True