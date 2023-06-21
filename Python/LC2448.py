class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        total, cur = sum(cost), 0
        target = 0
        
        for n, c in arr:
            cur += c
            if cur > total // 2:
                target = n
                break

        res = 0
        for n, c in arr:
            res += c * abs(n - target)

        return res
