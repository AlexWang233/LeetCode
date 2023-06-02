class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curPrice = 10000
        profit = 0
        for p in prices:
            if p > curPrice:
                profit += (p - curPrice)
            curPrice = p
        return profit