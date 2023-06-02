class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        l = len(questions)
        dp = [questions[i][0] for i in range(l)]
        for i in range(l - 2, -1, -1):
            n = questions[i][1]
            if n + i >= l - 1:
                dp[i] = max(dp[i + 1], dp[i])
                continue
            dp[i] = max(dp[i + 1], dp[i] + dp[i + n + 1])
        return dp[0]