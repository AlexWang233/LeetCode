class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        # Assign groups to those without
        for u in range(len(group)):
            if group[u] == -1:
                group[u] = m
                m += 1

        # Construct degree and order graphs for nodes and groups
        node_graph = [[] for _ in range(n)]
        node_degree = [0] * n
        group_graph = [[] for _ in range(m)]
        group_degree = [0] * m
        for u in range(n):
            for v in beforeItems[u]:
                node_graph[v].append(u)
                node_degree[u] += 1
                if group[u] != group[v]:
                    group_graph[group[v]].append(group[u])
                    group_degree[group[u]] += 1

        # Helper function to construct group/node order
        def getOrder(graph, degree):
            ans = []
            stack = [node for node in range(len(graph)) if degree[node] == 0]
            while stack:
                u = stack.pop()
                ans.append(u)
                for v in graph[u]:
                    degree[v] -= 1
                    if degree[v] == 0:
                        stack.append(v)
            if len(ans) < len(graph):
                return False
            return ans

        # Check whether there exists valid group/node order
        order_node = getOrder(node_graph, node_degree)
        order_group = getOrder(group_graph, group_degree)
        if not order_node or not order_group:
            return []

        # Orders nodes within each group
        order = defaultdict(list)
        for node in order_node:
            order[group[node]].append(node)

        # Construct result list with group order
        res = []
        for group in order_group:
            res += order[group]

        return res