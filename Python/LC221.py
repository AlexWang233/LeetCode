class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r, c = len(matrix), len(matrix[0])
        ans = 0
        for i in range(r):
            for j in range(c):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 0:
                    continue
                if i > 0 and j > 0:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])+1
                
                ans = max(matrix[i][j], ans)
        return ans * ans
                

                    