class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        l = len(nums) // 3 
        hp = [-n for n in nums[:l]]
        cur = sum(hp)
        heapify(hp)
        dp = []
        for i in range(l + 1):
            dp.append(cur)
            n = -nums[l + i]
            heappush(hp, n)
            cur = cur + n - heappop(hp)

        hp = nums[2 * l:]
        cur = sum(hp)
        heapq.heapify(hp)
        for i in range(l + 1):
            dp[~i] += cur
            n = nums[~(l + i)]
            heappush(hp, n)
            cur = cur + n - heappop(hp)

        return -max(dp)