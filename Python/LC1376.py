class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        child = [[] for _ in range(len(manager))]
        for i, m in enumerate(manager):
            if m > -1:
                child[m].append(i)

        def dfs(i: int):
            return max([dfs(j) for j in child[i]] + [0]) + informTime[i]

        return dfs(headID)