class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cur_max = 0
        d = defaultdict(lambda: 0)
        for n in nums:
            d[n] += 1
            if d[n] > cur_max:
                cur_max = d[n]

        res = 0
        for val in d.values():
            if val == cur_max:
                res += val
        return res