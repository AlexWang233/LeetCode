class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1
        
        x = abs(sx - fx)
        y = abs(sy - fy)
        return t >= max(x, y)