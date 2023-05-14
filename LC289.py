class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])
        neighbor = []

        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                neighbor.append((i - 1, j - 1))

        for i in range(r):
            for j in range(c):
                count = 0
                for x, y in neighbor:
                    a, b = i + x, j + y
                    if a < 0 or a >= r or b < 0 or b >= c:
                        continue
                    if board[a][b] % 2:
                        count += 1
                if board[i][j] == 1 and 3 >= count >= 2:
                    board[i][j] += 2
                elif board[i][j] == 0 and count == 3:
                    board[i][j] += 2

        for i in range(r):
            for j in range(c):
                board[i][j] >>= 1
