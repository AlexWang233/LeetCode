class Solution:
    def strangePrinter(self, s: str) -> int:
        l = len(s)
        s2 = ''
        for a, b in zip(s, ' '+s):
            if a != b:
                s2 += a
        
        l = len(s2)
        dp = [[100] * l for _ in range(l)]
        for i in range(l):
            dp[i][i] = 1

        for i in range(1, l):
            for j in range(i-1, -1, -1):

                if i - j == 1:
                    dp[j][i] = 1 if s2[i] == s2[j] else 2
                    continue

                for p in range(j, i):
                    dp[j][i] = min(dp[j][i], dp[j][p] + dp[p+1][i])

                if s2[j] == s2[i]:
                    dp[j][i] -= 1

        return dp[0][-1]