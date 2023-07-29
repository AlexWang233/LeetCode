class Solution:
    d = {}
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1
        def rec(a, b):
            if (a, b) in self.d:
                return self.d[(a, b)]
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            self.d[(a, b)] = (rec(a-4, b) + rec(a-3, b-1) + rec(a-2, b-2) + rec(a-1, b-3)) / 4
            return self.d[(a, b)]
        m = math.ceil(n / 25)
        return rec(m, m)