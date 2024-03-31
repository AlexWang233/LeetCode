class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        left = right = j = -1
        for i, n in enumerate(nums):
            if not minK <= n <= maxK:
                j = i
            if n == minK:
                left = i
            if n == maxK:
                right = i
            res += max(0, min(left, right) - j)
        return res