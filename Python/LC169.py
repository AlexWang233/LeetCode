class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        me = 0
        for n in nums:
            if c == 0:
                me = n
            c += 1 if me == n else -1
        return me
            