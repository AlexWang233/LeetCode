class Solution:
    def isSymmetric(self, n: int) -> bool:
        s = str(n)
        l = len(s)
        if (l % 2):
            return False
        l_sum = r_sum = 0
        for i in range(l // 2):
            l_sum += int(s[i])
            r_sum += int(s[~i])

        return l_sum == r_sum
        
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            res += self.isSymmetric(i)
        return res