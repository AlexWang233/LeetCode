class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(set)
        res = [0] * n
        count = [1] * n

        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)

        def dfs(node, prev):
            for n2 in tree[node]:
                if n2 != prev:
                    dfs(n2, node)
                    count[node] += count[n2]
                    res[node] += res[n2] + count[n2]

        def dfs2(node, prev):
            for n2 in tree[node]:
                if n2 != prev:
                    res[n2] = res[node] + n 
                    res[n2] -= 2 * count[n2]
                    dfs2(n2, node)

        dfs(0, -1)
        dfs2(0, -1)
        return res