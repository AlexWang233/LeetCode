class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        l = res = len(nums)
        res += 1
        start = cur = 0

        for end in range(l):
            cur += nums[end]
            while start <= end and cur > target:
                cur -= nums[start]
                start += 1
            if cur == target:
                res = min(res, l - end + start - 1)

        return -1 if res > l else res
        
