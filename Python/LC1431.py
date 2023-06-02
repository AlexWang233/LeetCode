class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        curMax = max(candies)
        ans = [item + extraCandies >= curMax for item in candies]
        return ans
