class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        
        start = ans = 0
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            while prod >= k:
                prod = prod // nums[start]
                start += 1

            ans += i - start + 1

        return ans