class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        count = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                count += 1
            if count > 1:
                if nums[start] == 0:
                    count -= 1
                start += 1
        return end - start
