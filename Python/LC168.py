class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            n = columnNumber % 26
            if n == 0:
                n += 26
                columnNumber -= 26
            c = chr(n - 1 + ord('A'))
            res = c + res
            columnNumber //= 26
        return res