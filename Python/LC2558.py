class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        arr = [-x for x in gifts]
        heapify(arr)
        cur = 1 << 32
        i = 0
        while i < k and cur > 1:
            cur = -heappop(arr)
            heappush(arr, -isqrt(cur))
            i += 1
        return -sum(arr)