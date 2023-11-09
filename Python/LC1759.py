class Solution:
    def countHomogenous(self, s: str) -> int:

        l = len(s)
        count = 1
        res = 1
        mod = 10 ** 9 + 7

        for i in range(1, l):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            res += count

        return res % mod
            