class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        prev = nums[0]
        count = 0
        res = 0
        for n in nums:
            if n > prev:
                count += 1
                prev = n
            res += count
        
        return res