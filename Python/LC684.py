class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = list(range(len(edges) + 1))
        def find_root(node):
            if root[node] != node:
                root[node] = find_root(root[node])
            return root[node]

        for n1, n2 in edges:
            r1, r2 = find_root(n1), find_root(n2)
            if r1 == r2:
                return [n1, n2]
            root[r2] = r1

        return [-1, -1] 