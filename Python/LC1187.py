class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        dp = {-1 : 0}
        
        for num in arr1:
            cur = defaultdict(lambda: float('inf'))
            for key in dp:
                if num > key:
                    cur[num] = min(cur[num], dp[key])
                j = bisect.bisect_right(arr2, key)
                if j < len(arr2):
                    cur[arr2[j]] = min(cur[arr2[j]], dp[key] + 1)
            dp = cur

        if dp:
            return min(dp.values())

        return -1