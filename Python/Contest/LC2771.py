class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        l = len(nums1)
        dp = [[1, 1] for _ in range(l)]
        arr = [[n1, n2] for n1, n2 in zip(nums1, nums2)]
        res = 1
        for i in range(1, l):
            for j in range(2):
                for k in range(2):
                    if arr[i][j] >= arr[i-1][k]:
                        dp[i][j] = max(dp[i][j], dp[i-1][k] + 1)
                        res = max(res, dp[i][j])
        
        return res