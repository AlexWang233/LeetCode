class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = 0
        while l < r:
            if nums[l] + nums[r] < target:
                res += (r - l)
                l += 1
            else:
                r -= 1
        return res