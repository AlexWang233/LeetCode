class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[-1000000] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j], 0) + nums1[j] * nums2[i]
                dp[i + 1][j + 1] = max([dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1]])

        return dp[-1][-1]