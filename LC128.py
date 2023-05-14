class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for n in nums:
            if n - 1 not in nums:
                m = n
                while m + 1 in nums:
                    m += 1
                ans = max(ans, m - n + 1)
        return ans