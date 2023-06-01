class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def gcd(m, n):
            return m if not n else gcd(n, m%n)

            
        def getslope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            
            if dx == 0: return (p1[0], 0)
            if dy == 0: return (0, p1[1])
            
            d = gcd(dx, dy)
            return (dx//d, dy//d)

        res = 1
        l = len(points)
        for i in range(l):
            d = defaultdict(lambda:0)
            same, maxi = 1, 0
            p1 = points[i]
            for j in range(i+1, l):
                p2 = points[j]
                if p1 == p2:
                    same += 1
                else:
                    slope = getslope(p1, p2)
                    d[slope] += 1
                    maxi = max(maxi, d[slope])
            res = max(res, maxi + same)

        return res

        return max(d[slope]) + 1