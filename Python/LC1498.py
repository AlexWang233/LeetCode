class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10 ** 9 + 7
        l = len(nums)
        right = l - 1
        ans = 0
        left = 0

        while left <= right:
            n = nums[left] + nums[right]
            if n > target:
                right -= 1
            else:
                ans += pow(2, right-left, mod)
                left += 1

        return ans % mod