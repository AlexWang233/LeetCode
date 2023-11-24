class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l = len(piles)
        i = l // 3
        res = 0
        while i + 1 < l:
            res += piles[i]
            i += 2

        return res