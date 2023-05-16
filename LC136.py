class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = 0
        for n in nums:
            m = m^n
        return m