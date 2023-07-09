class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        hp = []

        # Note that we're interested in adjacent pairs' sums
        for i in range(len(weights) - 1):
            heapq.heappush(hp, weights[i] + weights[i+1])

        # We don't care about the starting and ending elements since they're in every selection
        maxScore = sum(heapq.nlargest(k-1, hp))
        minScore = sum(heapq.nsmallest(k-1, hp))
        return maxScore - minScore