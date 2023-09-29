class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = True, True
        num = nums[0]
        for item in nums:
            inc = inc and item >= num
            dec = dec and item <= num
            num = item
        return inc or dec