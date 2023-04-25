class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)
        while len(h) > 1:
            s = heapq.heappop(h) - heapq.heappop(h)
            if not s == 0:
                heapq.heappush(h, s)

        if len(h) == 0:
            return 0
        else:
            return -h[0]