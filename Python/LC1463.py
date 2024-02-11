class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [[-1] * (c + 2) for _ in range(c + 2)]
        dp[1][-2] = grid[0][0] + grid[0][-1]

        def calcCherry(r1, r2):
            ans = -1
            for i in range(3):
                for j in range(3):
                    ans = max(ans, dp[r1 + i][r2 + j])
            return ans

        for i in range(1, r):
            temp = [[-1] * (c + 2) for _ in range(c + 2)]
            for j in range(c):
                for k in range(c):
                    prev = calcCherry(j, k)
                    if prev == -1:
                        continue
                    cur = grid[i][j] + grid[i][k]
                    if j == k:
                        cur //= 2
                    temp[j + 1][k + 1] = prev + cur
            dp = temp

        res = max([max(dp[i]) for i in range(c + 2)])
        return res
                    
                    
                