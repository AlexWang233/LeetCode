from collections import defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        edges = [[[], []] for _ in range(n)]
        for i, j in redEdges:
            edges[i][0].append(j)
        for i, j in blueEdges:
            edges[i][1].append(j)
        ans = [[0, 0]] + [[2*n, 2*n] for _ in range(n-1)]
        curLevel = [[0, 0], [0, 1]]
        while len(curLevel) > 0:
            nextLevel = []
            for prev, direction in curLevel:
                for cur in edges[prev][direction]:
                    if ans[cur][direction] == 2*n:
                        ans[cur][direction] = ans[prev][1 - direction] + 1
                        nextLevel.append([cur, 1 - direction])
            curLevel = nextLevel

        return [x if x < 2*n else -1 for x in map(min, ans)]
            