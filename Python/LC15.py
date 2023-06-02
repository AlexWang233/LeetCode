class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = []
        nums.sort()
        for i in range(l - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, l - 1
            while left < right:
                n = nums[i] + nums[left] + nums[right]
                if n > 0:
                    right -= 1
                elif n < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    right -= 1

        return ans
