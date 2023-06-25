class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        l = len(locations)
        dp = [[0] * fuel for _ in range(l)]
        target = locations[finish]

        def dfs(cur, fuel_left):
            if fuel_left < abs(locations[cur] - target):
                return 0
            if dp[cur][fuel_left - 1]:
                return dp[cur][fuel_left - 1]
            res = 0
            if cur == finish:
                res += 1
            for i in range(l):
                if i == cur:
                    continue
                res += dfs(i, fuel_left - abs(locations[cur] - locations[i]))
            res %= 10 ** 9 + 7
            dp[cur][fuel_left - 1] = res
            return res

        return dfs(start, fuel)