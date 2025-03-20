class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = list(range(n))

        min_walk = [-1] * n

        def find_root(node):
            if parent[node] != node:
                parent[node] = find_root(parent[node])
            return parent[node]

        for src, tgt, w in edges:
            # do bitwise and on all edges in each connected component
            # min walk from any nodes in same connected component is the same
            src_root = find_root(src)
            tgt_root = find_root(tgt)

            min_walk[tgt_root] &= w

            if src_root != tgt_root:
                min_walk[tgt_root] &= min_walk[src_root]
                parent[src_root] = tgt_root

        res = []

        for start, end in query:
            if start == end:
                res.append(0)
            elif find_root(start) != find_root(end):
                # disconnected components
                res.append(-1)
            else:
                res.append(min_walk[find_root(start)])

        return res