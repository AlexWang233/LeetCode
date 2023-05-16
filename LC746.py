class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        skip, step = 0, 0
        for n in cost:
            m = min(skip, step) + n
            skip = step
            step = m
        return min(skip, step)