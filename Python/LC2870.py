class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp = Counter(nums)
        res = 0
        for i in mp.values():
            if i == 1:
                return -1
            if i % 3:
                res += 1
            res += i // 3
        return res