class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        l = [1, 2]
        for i in range(n - 2):
            n = l[0] + l[1]
            l[0] = l[1]
            l[1] = n
        return l[1]