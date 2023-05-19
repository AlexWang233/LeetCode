class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c1 = c2 = mask = 0
        for n in nums:
            c2 ^= c1 & n
            c1 ^= n
            mask = ~(c1 & c2)
            c2 &= mask
            c1 &= mask
        return c1