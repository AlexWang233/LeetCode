class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        l = len(nums)
        last = nums[-1]
        res = 0
        for i in range(l - 2, -1, -1):
            if nums[i] > last:
                cur = nums[i] // last
                if nums[i] % last > 0:
                    cur += 1
                last = nums[i] // cur
                res += (cur - 1)
            else:
                last = nums[i]
        return res