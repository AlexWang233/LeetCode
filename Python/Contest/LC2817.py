class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0
        arr = []
        res = 10 ** 9
        for i in range(x, len(nums)):
            bisect.insort_left(arr, nums[i - x])
            n = nums[i]
            ind = bisect.bisect(arr, n)
            if ind > 0:
                res = min(res, abs(n - arr[ind - 1]))
            if ind < len(arr):
                res = min(res, abs(arr[ind] - n))
        return res