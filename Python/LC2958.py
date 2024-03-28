class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = Counter()
        res = i = 0
        for j in range(len(nums)):
            n = nums[j]
            count[n] += 1
            while count[n] > k:
                count[nums[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res