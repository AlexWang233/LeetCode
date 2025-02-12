class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        m = defaultdict(lambda: 0)
        ans = -1
        def sd(n):
            res = 0
            while n:
                res += n % 10
                n //= 10
            return res
        for n in nums:
            s = sd(n)
            if s in m:
                ans = max(ans, m[s] + n)
                m[s] = max(m[s], n)
            else:
                m[s] = n
        return ans

