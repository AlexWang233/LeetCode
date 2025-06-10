class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = 0
        min_even = len(s)
        c = Counter(s)
        for val in c.values():
            if val % 2 == 1:
                max_odd = max(max_odd, val)
            else:
                min_even = min(min_even, val)
        return max_odd - min_even