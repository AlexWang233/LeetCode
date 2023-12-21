class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xarr = [x for x, y in points]
        xarr.sort()
        res = max([xarr[i + 1] - xarr[i] for i in range(len(xarr) - 1)])
        return res