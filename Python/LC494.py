class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d = defaultdict(lambda: 0)
        d[0] = 1
        for n in nums:
            nd = defaultdict(lambda: 0)
            for key in d.keys():
                nd[key + n] += d[key]
                nd[key - n] += d[key]
            d = nd
        return d[target]