class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        l = sorted((e[0], i) for i, e in enumerate(intervals))
        m = len(intervals)
        ans = []
        for item in intervals:
            r = bisect.bisect_left(l, (item[1], 0))
            if r < m:
                ans.append(l[r][1])
            else:
                ans.append(-1)
        return ans