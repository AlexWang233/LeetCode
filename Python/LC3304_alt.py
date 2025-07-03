class Solution:
    def kthCharacter(self, k: int) -> str:

        def helper(i):
            res = 0
            while i > 0:
                res += (i % 2)
                i >>= 1
            return res

        ans = helper(k - 1)

        return chr(ord('a') + ans)