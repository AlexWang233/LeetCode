class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l = len(dist)        
        left, right = 1, 10 ** 7 + 1

        def isFeasible(speed: int):
            t = dist[-1] / speed + sum((dist[i] + speed - 1) // speed for i in range(l - 1))
            return t <= hour

        while left < right:
            mid = (left + right)//2
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1

        return -1 if right == 10 ** 7 + 1 else right