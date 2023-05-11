class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        curLeft = height[left]
        curRight = height[right]
        ans = min(curLeft, curRight) * (right - left)
        while left < right:
            if curLeft > curRight:
                right -= 1
                if height[right] > curRight:
                    curRight = height[right]
            else:
                left += 1
                if height[left] > curLeft:
                    curLeft = height[left]
            ans = max(ans, min(curLeft, curRight) * (right - left))

        return ans