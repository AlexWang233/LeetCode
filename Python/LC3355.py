class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        arr = [0] * (len(nums) + 1)
        for start, end in queries:
            arr[start] += 1
            arr[end + 1] -= 1
        cur = 0
        for i, n in enumerate(nums):
            cur += arr[i]
            if n > cur:
                return False
        return True