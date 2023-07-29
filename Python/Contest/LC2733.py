class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        curMin = 100
        curMax = 1
        if len(nums) <= 2:
            return -1
        for n in nums:
            if n < curMin:
                curMin = n
            if n > curMax:
                curMax = n
        for n in nums:
            if n != curMin and n != curMax:
                return n
        return -1