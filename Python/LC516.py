class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        dp, prevDp = [0] * l, [0] * l
        for i in range(l - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, l):
                if s[i] == s[j]:
                    dp[j] = prevDp[j-1] + 2
                else:
                    dp[j] = max(prevDp[j], dp[j-1])
            dp, prevDp = [0] * l, dp

        return prevDp[-1]