class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 0
        cur = 1
        while n > 0:
            if n % 2 == 0:
                ans += cur
            n //= 2
            cur *= 2
        return ans