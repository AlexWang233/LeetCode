class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        m = tickets[k]
        for i, n in enumerate(tickets):
            if i > k:
                res += min(n, m - 1)
            else:
                res += min(n, m)

        return res