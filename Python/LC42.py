class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ml, mr = height[0], height[-1]
        l, r = 1, n - 2
        ans = 0
        while l <= r:
            if ml < mr:
                if height[l] > ml:
                    ml = height[l]
                else:
                    ans += ml - height[l]
                l += 1
            else:
                if height[r] > mr:
                    mr = height[r]
                else:
                    ans += mr - height[r]
                r -= 1
        return ans