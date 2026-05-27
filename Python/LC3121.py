class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = upper = 0
        valid = (1 << 27) - 1
        for i, c in enumerate(word):
            temp = ord(c)
            if temp < ord("a"):
                upper |= 1 << (temp - ord("A"))
            else:
                idx = 1 << (temp - ord("a"))
                if upper & idx:
                    valid &= ~idx
                else:
                    lower |= idx

        # print(lower)
        # print(upper)
        # print(valid)

        ans = (lower & upper & valid).bit_count()
        return ans
