class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = defaultdict(lambda: 0)
        for n in nums:
            d[n] += 1
        
        res = 0
        for occ in d.values():
            res += (occ * (occ - 1)) // 2

        return res
            