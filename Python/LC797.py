class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(i: int, path: List[int]):
            if i == l - 1:
                ans.append(path)
            else:
                for j in graph[i]:
                    dfs(j, path + [j])

        ans = []
        l = len(graph)

        dfs(0, [0])
        return ans