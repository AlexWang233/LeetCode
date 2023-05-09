class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        ans = 1
        curEnd = points[0][1]
        for start, end in points:
            if start > curEnd:
                curEnd = end
                ans += 1
        return ans