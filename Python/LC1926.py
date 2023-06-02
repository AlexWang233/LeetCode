class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        i, j = entrance
        bfsArr = [(i, j)]
        maze[i][j] = '+'
        m, n = len(maze), len(maze[0])
        ans = 0
        while len(bfsArr) > 0:
            newArr = []
            while len(bfsArr) > 0:
                x, y = bfsArr.pop()
                for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if i < 0 or j < 0 or i >= m or j >= n:
                        if ans > 0:
                            return ans
                        else:
                            continue
                    if maze[i][j] == '.':
                        maze[i][j] = '+'
                        newArr.append((i, j))
            ans += 1
            bfsArr = newArr

        return -1
