class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        save = [(0, i) for i in range(n)]
        save += [(m - 1, i) for i in range(n)]
        save += [(j, 0) for j in range(m)]
        save += [(j, n - 1) for j in range(m)]
        while save:
            x, y = save.pop()
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                board[x][y] = 'I'
                save += [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 'I' else 'X'
                