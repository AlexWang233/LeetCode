class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda x: x[1])
        prevDp, dp = [[0, 0]], [[0, 0]]
        for _ in range(k):
            for start, end, val in events:
                i = bisect.bisect(prevDp, [start]) - 1
                if prevDp[i][1] + val > dp[-1][1]:
                    dp.append([end, prevDp[i][1] + val])
            prevDp, dp = dp, [[0, 0]]
        return prevDp[-1][-1]