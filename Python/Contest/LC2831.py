class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        res = i = 0
        count = Counter()
        for j in range(len(nums)):
            count[nums[j]] += 1
            res = max(res, count[nums[j]])
            if j - i + 1 - res > k:
                count[nums[i]] -= 1
                i += 1
        return res