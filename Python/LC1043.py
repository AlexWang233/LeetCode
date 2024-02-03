class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        l = len(arr)
        dp = [0] * (l + 1)
        for i in range(1, l + 1):
            cur = 0
            l2 = min(k, i)
            for j in range(1, l2 + 1):
                cur = max(cur, arr[i - j])
                dp[i] = max(dp[i], dp[i-j] + cur * j)
        return dp[-1]