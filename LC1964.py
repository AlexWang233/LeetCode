class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        l = [10**7 + 1] * len(obstacles)
        ans = []
        for i in obstacles:
            p = bisect_right(l, i)
            ans.append(p + 1)
            l[p] = i
        return ans