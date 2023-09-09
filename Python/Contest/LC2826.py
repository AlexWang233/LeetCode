class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a = b = c = 0
        for x in nums:
            a += (x != 1)
            b = min(a, b + (x != 2))
            c = min(b, c + (x != 3))
        return c
