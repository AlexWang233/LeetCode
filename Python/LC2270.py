class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        arr = list(accumulate(nums))
        ans = 0
        for i in range(len(nums) - 1):
            if arr[i] >= arr[-1] - arr[i]:
                ans += 1
        return ans