class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])
        ans = []
        for [start, end] in intervals:
            if len(ans) > 0 and start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])

        return ans