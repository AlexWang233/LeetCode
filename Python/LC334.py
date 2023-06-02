class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        m1 = m2 = 2**31
        for n in nums:
            if n > m2:
                return True
            elif n <= m1:
                m1 = n
            else:
                m2 = n
        return False