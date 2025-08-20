class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cur = ans = 0
        for n in nums:
            if n == 0:
                cur += 1
                ans += cur
            else:
                cur = 0
        return ans