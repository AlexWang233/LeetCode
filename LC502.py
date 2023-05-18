class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        hp = []
        arr = sorted(zip(profits, capital), key = lambda x: x[1])
        i = 0
        for _ in range(k):
            while i < len(arr) and arr[i][1] <= w:
                heapq.heappush(hp, -arr[i][0])
                i += 1
            if hp:
                w -= heapq.heappop(hp)
        return w