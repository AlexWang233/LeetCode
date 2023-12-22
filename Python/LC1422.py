class Solution:
    def maxScore(self, s: str) -> int:
        counter = Counter(s)
        ones = counter["1"]
        res = zeros = 0

        for c in s[:-1]:
            if c == "0":
                zeros += 1
            else:
                ones -= 1
            res = max(res, zeros + ones)

        return res
                