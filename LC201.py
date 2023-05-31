class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0 or right == 0:
            return 0
        n = 1
            
        while n*2 <= right:
            n *= 2
        
        return self.rangeBitwiseAnd(left - n, right - n) + (n if left >= n else 0)

