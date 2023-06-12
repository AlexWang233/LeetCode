class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(set)
        res = set([])
        # set up bi-directional graph
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
            # remember all edges
            if u < v:
                res.add((u, v))
            else:
                res.add((v, u))

        level = [-1] * n

        def dfs(node, depth, parent):
            if level[node] > 0:
                return level[node]
            level[node] = depth
            min_depth = n + 1
            for ngbr in graph[node]:
                # don't go back to parent right away
                if ngbr == parent:
                    continue
                # find depth of ngbr without this edge
                back_depth = dfs(ngbr, depth + 1, node)
                # if exists back path, this edge is in cycle
                if back_depth <= depth:
                    res.discard((node, ngbr))
                    res.discard((ngbr, node))
                min_depth = min(min_depth, back_depth)
            # return back path minimum depth
            return min_depth

        dfs(0, 1, -1)
        return list(res)
            