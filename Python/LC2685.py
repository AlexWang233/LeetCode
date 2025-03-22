class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find_root(node):
            if parent[node] != node:
                parent[node] = find_root(parent[node])
            return parent[node]

        for u, v in edges:
            root_u = find_root(u)
            root_v = find_root(v)
            if root_u != root_v:
                parent[root_v] = root_u

        component_nodes = {}
        component_edges = {}
        roots = [-1] * n
        for i in range(n):
            roots[i] = find_root(i)
            if roots[i] not in component_nodes:
                component_nodes[roots[i]] = set()
                component_edges[roots[i]] = 0
            component_nodes[roots[i]].add(i)

        for u, v in edges:
            component_edges[roots[u]] += 1

        res = 0
        for root in component_nodes:
            V = len(component_nodes[root])
            E = V * (V - 1) // 2
            if component_edges[root] == E:
                res += 1

        return res
        
