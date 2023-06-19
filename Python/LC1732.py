class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curAlt = 0
        ans = 0
        for i in gain:
            curAlt += i
            ans = max(ans, curAlt)
        return ans