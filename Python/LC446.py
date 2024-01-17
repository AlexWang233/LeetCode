class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0

        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                c = dp[j][d]
                dp[i][d] += c + 1
                ans += c

        return ans