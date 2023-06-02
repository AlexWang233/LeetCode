class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        fc = False
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            if matrix[i][0] == 0:
                fc = True
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(r - 1, -1, -1):
            for j in range(c - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if fc:
                matrix[i][0] = 0