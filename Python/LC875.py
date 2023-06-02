class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            count = 0
            for n in piles:
                count += -(-n // mid)

            if count > h:
                left = mid + 1
            else:
                right = mid

        return right