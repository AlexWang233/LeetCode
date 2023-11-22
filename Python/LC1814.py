class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            m = 0
            while n > 0:
                m *= 10
                m += n % 10
                n //= 10
            return m

        l = len(nums)
        arr = [n - rev(n) for n in nums]
        count = defaultdict(lambda: 0)
        res = 0

        for n in arr:
            res += count[n]
            count[n] += 1

        return res % (10 ** 9 + 7)