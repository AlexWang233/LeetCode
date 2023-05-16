class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ans = 0
        curMin = prices[0]
        for n in prices[1:]:
            if n < curMin:
                curMin = n
            elif n > curMin + fee:
                ans += n - curMin - fee
                curMin = n - fee
            
        return ans