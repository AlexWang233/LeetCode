class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # 1. find where stones rest in each row and move them
        n, m = len(boxGrid), len(boxGrid[0])

        for i in range(n):
            cur = m - 1
            for j in range(m - 1, -1, -1):
                if boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][cur] = '#'
                    cur -= 1
                elif boxGrid[i][j] == '*':
                    cur = j - 1
                else:
                    boxGrid[i][j] = '.'

        ans = [list(row) for row in zip(*boxGrid[::-1])]
        return ans