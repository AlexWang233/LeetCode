class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        m = purchaseAmount % 10
        if m >= 5:
            purchaseAmount += (10 - m)
        else:
            purchaseAmount -= m
        return 100 - purchaseAmount