class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        l = len(colors)
        for i in range(l - 1, 0, -1):
            if colors[i] != colors[0]:
                ans = i
                break
        for i in range(1, l):
            if colors[i] != colors[-1]:
                ans = max(ans, l - i - 1)
                break
        return ans
