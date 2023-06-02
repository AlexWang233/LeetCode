import queue

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = len(nums) + 1
        curr = 0
        left = 0
        for i in range(len(nums)):
            curr += nums[i]
            while curr >= target:
                shortest = min(shortest, i - left + 1)
                curr -= nums[left]
                left += 1
        if shortest > len(nums):
            return 0
        return shortest