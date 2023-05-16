class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda arr : arr[1])
        ans = 0
        curMax = -10**5
        for start, end in intervals:
            if start < curMax:
                ans += 1
            else:
                curMax = end
        return ans