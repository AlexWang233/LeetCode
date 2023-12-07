class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = -1
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                res = i
                break

        return num[:res+1]