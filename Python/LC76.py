class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        m = len(t)

        l = L = R = 0

        for r, c in enumerate(s, 1):
            if counter[c] > 0:
                m -= 1
            counter[c] -= 1
            if m == 0:
                while l < r and counter[s[l]] < 0:
                    counter[s[l]] += 1
                    l += 1
                if R == 0 or r - l <= R - L:
                    L, R = l, r
        return s[L:R]