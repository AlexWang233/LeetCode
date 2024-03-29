class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        res = cur = i = 0
        for j in range(len(nums)):
            if nums[j] == m:
                cur += 1
            while cur >= k:
                if nums[i] == m:
                    cur -= 1
                i += 1
            res += i
        return res