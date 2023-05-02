class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(a, b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count == 2 or count == 0

        def dfs(i):
            visited[i] = True
            for j in range(len(strs)):
                if visited[j]:
                    continue
                if isSimilar(strs[i], strs[j]):
                    dfs(j)

        visited = [False] * len(strs)
        ans = 0
        for i in range(len(strs)):
            if visited[i]:
                continue
            ans += 1
            dfs(i)

        return ans
