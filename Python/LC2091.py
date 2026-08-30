class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        minInd = maxInd = 0
        curMin, curMax = 10 ** 5, -10 ** 5
        for i, n in enumerate(nums):
            if n <= curMin:
                curMin = n
                minInd = i
            if n >= curMax:
                curMax = n
                maxInd = i
        n = len(nums)
        mi, ma = min(minInd, maxInd), max(minInd, maxInd)
        ans = min(ma + 1, n - mi)
        ans = min(ans, n - ma + mi + 1)
        return ans
            