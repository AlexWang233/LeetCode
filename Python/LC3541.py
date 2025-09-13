class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        VOWELS = "aeiou"
        vow = con = 0
        for k, v in c.items():
            if k in VOWELS:
                vow = max(vow, v)
            else:
                con = max(con, v)
        return vow + con