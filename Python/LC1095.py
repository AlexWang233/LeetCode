# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        l, r = 0, n - 1
        peak = -1
        while l < r:
            m = (l + r) // 2
            if mountain_arr.get(m) < mountain_arr.get(m + 1):
                l = peak = m + 1
            else:
                r = m

        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            if mountain_arr.get(m) < target:
                l = m + 1
            elif mountain_arr.get(m) > target:
                r = m - 1
            else:
                return m

        l, r = peak, n - 1
        while l <= r:
            m = (l + r) // 2
            if mountain_arr.get(m) > target:
                l = m + 1
            elif mountain_arr.get(m) < target:
                r = m - 1
            else:
                return m

        return -1
            
