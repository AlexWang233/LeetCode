class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        cur_min = nums[0]
        ans = -1
        for n in nums[1:]:
            if n <= cur_min:
                cur_min = n
            else:
                ans = max(ans, n - cur_min)
        return ans