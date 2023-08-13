class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        res = -1
        for n in nums:
            digit = int(max(str(n)))
            d[digit].append(n)

        for digit in d:
            if len(d[digit]) > 1:
                d[digit].sort()
                res = max(res, d[digit][-1] + d[digit][-2])

        return res