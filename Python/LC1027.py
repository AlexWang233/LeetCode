class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: 1)
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i+1, len(nums)):
                y = nums[j]
                dp[(j, y - x)] = dp[(i, y - x)] + 1

        return max(dp.values()) 