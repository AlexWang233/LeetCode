class Solution:
    def countHillValley(self, nums: List[int]) -> int:

        left = ans = 0

        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                if nums[i] > nums[left] and nums[i] > nums[i + 1]:
                    ans += 1
                elif nums[i] < nums[left] and nums[i] < nums[i + 1]:
                    ans += 1
                left = i

        return ans
            