class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        cur_min = prices[0]
        res = money + 1

        for p in prices[1:]:
            if cur_min + p < res:
                res = cur_min + p
            if p < cur_min:
                cur_min = p

        return money if res > money else money - res