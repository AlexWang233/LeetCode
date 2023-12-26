class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        mod = 10 ** 9 + 7

        def rec(m, cur):
            if m == 1:
                return 1 if 0 < cur <= k else 0
            else:
                if (m, cur) in dp:
                    return dp[(m, cur)]
                dp[(m, cur)] = 0
                for i in range(1, k + 1):
                    dp[(m, cur)] += rec(m - 1, cur - i)
                dp[(m, cur)] %= mod
            return dp[(m, cur)]

        res = rec(n, target) % mod
        return res 