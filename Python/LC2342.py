class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        m = defaultdict(lambda: 0)
        ans = -1
        d = defaultdict(lambda: -1)
        def sd(n):
            res = 0
            while n:
                res += n % 10
                n //= 10
            return res
        for n in nums:
            s = sd(n)
            if s in m:
                d[s] = max(d[s], m[s] + n)
                m[s] = max(m[s], n)
                ans = max(ans, d[s])
            else:
                m[s] = n
        return ans

