class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda p: (-p[0], p[1]))
        # print(points)
        ans = 0
        l = len(points)
        for i in range(l - 1):
            y = 1 << 31
            for j in range(i + 1, l):
                if y > points[j][1] >= points[i][1]:
                    ans += 1
                    y = points[j][1]

        return ans