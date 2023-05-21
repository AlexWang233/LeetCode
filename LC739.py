from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans, curMax = [0] * len(temperatures), 0
        for i in range(len(temperatures)-1,-1,-1):
            t = temperatures[i]
            if t >= curMax:
                curMax = t
            else:
                d = 1
                while t >= temperatures[i + d]:
                    d += ans[i + d]
                ans[i] = d
        return ans