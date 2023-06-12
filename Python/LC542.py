class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        ans = [[10001]*c for i in range(r)]

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    if i > 0:
                        ans[i][j] = min(ans[i][j], ans[i-1][j]+1)
                    if j > 0:
                        ans[i][j] = min(ans[i][j], ans[i][j-1]+1)
        
        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                if ans[i][j] == 0:
                    continue
                if i < r-1:
                    ans[i][j] = min(ans[i][j], ans[i+1][j]+1)
                if j < c-1:
                    ans[i][j] = min(ans[i][j], ans[i][j+1]+1)

        return ans

