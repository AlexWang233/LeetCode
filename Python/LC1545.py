class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        curLen = 1
        reverse = False
        for i in range(n - 1):
            curLen *= 2
            curLen += 1
        #print(curLen)
        while n > 1:
            #print(n, reverse, k)
            curLen = (curLen - 1) // 2
            if k == curLen + 1:
                return "0" if reverse else "1"
            if k > curLen:
                k = (curLen + 1) * 2 - k
                reverse = not reverse
            n -= 1
        return "1" if reverse else "0"

