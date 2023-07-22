class Solution:
    def isGood(self, nums: List[int]) -> bool:
        count = c2 = 0
        l = len(nums)
        for n in nums:
            if n >= l:
                return False
            if n == l - 1:
                c2 += 1
            else:
                count |= (1 << (n - 1))
            
        return count == (1 << (l - 2)) - 1 and c2 == 2
            
            