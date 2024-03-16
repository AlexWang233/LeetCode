class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        l = len(nums)
        d = {0: -1}
        count = 0
        res = 0
        for i, n in enumerate(nums):
            if n == 0:
                count += 1
            else:
                count -= 1
            if count not in d:
                d[count] = i
            else:
                res = max(res, i - d[count])
        return res