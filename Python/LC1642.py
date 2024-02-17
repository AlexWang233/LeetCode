class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hp = []
        l = len(heights) - 1
        for i in range(l):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(hp, diff)
            if len(hp) > ladders:
                bricks -= heapq.heappop(hp)
            if bricks < 0:
                return i
        return l