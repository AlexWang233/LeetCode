class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = 10000
        for i, n in enumerate(nums):
            if n == target:
                ans = min(ans, abs(start - i))
        return ans
