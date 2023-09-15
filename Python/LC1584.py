class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def m_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        l = len(points)
        d = defaultdict(list)

        for i in range(l):
            for j in range(i + 1, l):
                dist = m_dist(points[i], points[j])
                d[i].append((dist, j))
                d[j].append((dist, i))

        cnt = 1
        res = 0
        visited = [True] + [False] * (l - 1)
        hp = d[0]
        heapify(hp)

        while hp and cnt < l:
            dist, i = heappop(hp)
            if not visited[i]:
                visited[i] = True
                cnt += 1
                res += dist
                for e in d[i]:
                    heappush(hp, e)
        
        return res
