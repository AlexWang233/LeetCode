class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x, y = points[0]
        res = 0
        for p in points[1:]:
            x_diff, y_diff = abs(x - p[0]), abs(y - p[1])
            res += max(x_diff, y_diff)
            x, y = p[0], p[1]

        return res