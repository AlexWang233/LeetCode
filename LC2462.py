class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        lq = costs[:candidates]
        rq = costs[max(candidates, len(costs) - candidates):]
        heapify(lq)
        heapify(rq)
        ans = 0
        l = len(lq)
        r = len(rq)
        for i in range(k):
            if not rq or (lq and lq[0] <= rq[0]):
                ans += heappop(lq)
                if l + r < len(costs):
                    heappush(lq, costs[l])
                    l += 1
            else:
                ans += heappop(rq)
                if l + r < len(costs):
                    heappush(rq, costs[~r])
                    r += 1
        return ans


