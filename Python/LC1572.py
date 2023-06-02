class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        l = len(mat)
        for i in range(l):
            ans += mat[i][i]
            if i != l - i - 1:
                ans += mat[i][l-i-1]
        return ans