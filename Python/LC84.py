class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        res = 0
        for i in heights + [-1]:
            total_w = 0
            while stk and stk[-1][1] >= i:
                w, h = stk.pop()
                total_w += w
                res = max(res, total_w * h)
            stk.append((total_w + 1, i))
        return res