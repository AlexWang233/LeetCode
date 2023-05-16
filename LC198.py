class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax, curMax = 0, 0
        for n in nums:
            m = max(prevMax + n, curMax)
            prevMax = curMax
            curMax = m
        return curMax