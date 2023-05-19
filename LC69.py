class Solution:
    def mySqrt(self, x: int) -> int:
        res = x
        while res * res > x:
            res = (res + x / res) / 2
        return int(res)