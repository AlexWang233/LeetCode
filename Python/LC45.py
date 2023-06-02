class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = prevMax = curMax = step = 0
        while curMax < len(nums) - 1:
            if i <= prevMax:
                curMax = max(curMax, i + nums[i])
            else:
                prevMax = curMax
                curMax = i + nums[i]
                step += 1
            i += 1
        return step + 1
        