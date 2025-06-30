class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left = right = 0
        ans = 0
        while right < len(nums):
            while left < len(nums) and nums[right] - nums[left] > 1:
                left += 1
            while right < len(nums) and nums[right] - nums[left] <= 1:
                right += 1
            if nums[right - 1] - nums[left] == 1:
                ans = max(ans, right - left)
        return ans