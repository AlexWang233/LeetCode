class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lower = 1
        upper = 2 ** 16
        while lower < upper:
            n = (lower + upper) // 2
            res = n * n
            if res == num:
                return True
            if res < num:
                lower = n + 1
            else:
                upper = n
        return False
                
