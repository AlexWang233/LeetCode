class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res = max(left)
        res = max

        for ant in right:
            res = max(res, n - ant)

        return res