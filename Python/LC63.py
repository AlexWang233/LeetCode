class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r, c = len(obstacleGrid), len(obstacleGrid[0])

        row = []
        for i in range(c):
            if obstacleGrid[0][i] == 1:
                row += [0] * (c - i)
                break
            row.append(1)

        for i in range(1, r):
            prevRow = row.copy()
            row[0] = 0 if obstacleGrid[i][0] else prevRow[0]
            for j in range(1, c):
                if obstacleGrid[i][j] == 1:
                    row[j] = 0
                else:
                    row[j] = prevRow[j] + row[j-1]

        return row[-1]

            