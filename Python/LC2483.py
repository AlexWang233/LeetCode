class Solution:
    def bestClosingTime(self, customers: str) -> int:
        counter = Counter(customers)
        cur = counter['Y']
        res = 0
        curMin = cur
        for i, c in enumerate(list(customers)):
            if c == 'Y':
                cur -= 1
            else:
                cur += 1
            if cur < curMin:
                res = i + 1
                curMin = cur
        return res