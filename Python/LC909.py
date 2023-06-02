class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        l = len(board)
        d = {1: 0}
        bfs = [1]
        for x in bfs:
            for i in range(x+1, x+7):
                a, b = (i - 1) // l, (i - 1) % l
                c = board[~a][b if not a % 2 else ~b]
                if c > 0:
                    i = c
                if i == l * l:
                    return d[x] + 1
                if i not in d:
                    d[i] = d[x] + 1
                    bfs.append(i)
        return -1