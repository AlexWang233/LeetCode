class Solution:
    def canCross(self, stones: List[int]) -> bool:
        l = len(stones)
        stones_set = set(stones)
        visited = set()
        def dfs(val, k):
            if (val + k not in stones_set) or ((val, k) in visited):
                return False
            if val + k == stones[-1]:
                return True
            visited.add((val, k))
            for i in range(3):
                j = k + i - 1
                if dfs(val + k, j):
                    return True
            return False
        return dfs(stones[0], 1)