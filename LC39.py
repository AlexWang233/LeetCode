class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(arr: List[int], m: int, ind: int) -> None:
            if m > target:
                return
            if m == target:
                ans.append(arr)

            for i in range(ind, l):
                dfs(arr + [candidates[i]], m + candidates[i], i)

        list(set(candidates)).sort()
        ans = []
        l = len(candidates)
        dfs([], 0, 0)
        return ans