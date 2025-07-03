class Solution:
    def kthCharacter(self, k: int) -> str:

        def pow_of_two(i):
            if i == 0:
                return -1
            res = 1
            while res * 2 <= i:
                res *= 2
            return res

        def helper(i):
            p = pow_of_two(i)
            if p == -1:
                return 0
            return helper(i - p) + 1

        ans = helper(k - 1) % 26

        return chr(ord('a') + ans)