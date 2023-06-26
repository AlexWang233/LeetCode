class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = len(arr)
        if arr[-1] < k:
            return k + l
        if arr[0] > k:
            return k
        l, r = 0, l
        while l < r:
            m = (l + r) // 2
            if arr[m] < k + m + 1:
                l = m + 1
            else:
                r = m
        return l + k