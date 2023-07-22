class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        maxArr = [-10 ** 7, -10 ** 7]
        maxArr[nums[0] % 2] = nums[0]
        for n in nums[1:]:
            if n % 2 == 0:
                maxArr[0] = max(maxArr[0] + n, maxArr[1] + n - x)
            else:
                maxArr[1] = max(maxArr[1] + n, maxArr[0] + n - x)
        return max(maxArr)