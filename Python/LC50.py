class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        pos = True
        if n < 0:
            pos = False
            n *= -1
        if pos:
            return self.myPow(x * x, n // 2) * self.myPow(x, n % 2)
        return 1 / (self.myPow(x * x, n // 2) * self.myPow(x, n % 2))