class Solution:
    def totalMoney(self, n: int) -> int:

        weeks = n // 7
        res = weeks * 28
        res += (weeks * (weeks - 1) * 7) // 2

        if n % 7 > 0:
            days = n % 7
            cur = weeks + 1
            for i in range(days):
                res += cur
                cur += 1

        return res