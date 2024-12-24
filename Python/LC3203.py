class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        adjList1 = self.buildAdjList(edges1)
        adjList2 = self.buildAdjList(edges2)

        d1 = self.topoSort(adjList1)
        d2 = self.topoSort(adjList2)

        sl1 = l1 = sl2 = l2 = 0

        if len(d1) == 2:
            sl1 = heapq.heappop(d1)
            l1 = heapq.heappop(d1)
        else:
            l1 = heapq.heappop(d1)

        if len(d2) == 2:
            sl2 = heapq.heappop(d2)
            l2 = heapq.heappop(d2)
        else:
            l2 = heapq.heappop(d2)

        return max(sl1 + l1, max(sl2 + l2, l1 + l2 + 1))

    def topoSort(self, adjList):
        inDegree = {key: len(adjList[key]) for key in adjList}
        q = deque()
        res = []

        for key in adjList:
            if inDegree[key] == 1:
                q.append((key, 0))
        
        while q:
            node, dist = q.popleft()
            for adj in adjList[node]:
                if inDegree[adj] > 1:
                    inDegree[adj] -= 1
                if inDegree[adj] == 1:
                    q.append((adj, dist + 1))
                    heapq.heappush(res, dist + 1)
                    if len(res) > 2:
                        heapq.heappop(res)

            inDegree[node] -= 1
            if not q:
                break
        if not res:
            res.append(0)
        return res

    def buildAdjList(self, edges):
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        return adjList


        