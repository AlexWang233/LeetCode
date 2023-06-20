class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = len(nums)
        if l < 2 * k + 1:
            return [-1] * l
        curSum = sum(nums[:2 * k + 1])
        res.append(curSum // (2 * k + 1))
        for i in range(k + 1, l - k):
            curSum += nums[i + k]
            if i < k:
                res.append(-1)
                continue
            curSum -= nums[i - k - 1]
            res.append(curSum // (2 * k + 1))
        
        res = [-1] * k + res + [-1] * k
        return res