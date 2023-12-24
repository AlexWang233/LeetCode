class Solution:
    def minOperations(self, s: str) -> int:
        alt1 = alt2 = 0
        cur = False
        for c in s:
            if c == '0':
                if cur:
                    alt1 += 1
                else:
                    alt2 += 1
            else:
                if cur:
                    alt2 += 1
                else:
                    alt1 += 1
            cur = not cur

        return min(alt1, alt2)