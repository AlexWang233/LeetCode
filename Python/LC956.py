class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(lambda: 0)
        dp[0] = 0
        for rod in rods:
            for diff, l in dp.copy().items():
                dp[diff + rod] = max(dp[diff + rod], l)
                dp[abs(diff - rod)] = max(dp[abs(diff - rod)], l + min(diff, rod))
        return dp[0]