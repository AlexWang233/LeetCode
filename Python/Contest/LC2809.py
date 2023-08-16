class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        l = len(nums1)
        dp = [0] * (l + 1)
        arr = sorted(zip(nums2, nums1))
        for i, (n, m) in enumerate(arr, 1):
            for j in range(i, 0, -1):
                dp[j] = max(dp[j], dp[j-1] + j*n+m) 

        a, b = sum(nums1), sum(nums2)
        for i in range(0, l + 1):
            if b * i + a - dp[i] <= x:
                return i
        return -1