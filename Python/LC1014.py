class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curMax = ans = 0
        for n in values:
            ans = max(ans, curMax + n)
            curMax = max(curMax, n) - 1
        return ans