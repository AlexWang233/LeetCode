class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = 10000
        curMax = 0
        for p in prices:
            if p < curMin:
                curMin = p
            elif p - curMin > curMax:
                curMax = p - curMin
        return curMax