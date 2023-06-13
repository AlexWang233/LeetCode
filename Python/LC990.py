class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = defaultdict(list)
        queue = []
        for eq in equations:
            if eq[1] == '=':
                graph[eq[0]].append(eq[3])
                graph[eq[3]].append(eq[0])
            else:
                queue.append((eq[0], eq[3]))

        visited = set()
        def dfs(start, end):
            if start == end:
                return False
            if start in visited:
                return True
            visited.add(start)
            return all(dfs(ngbr, end) for ngbr in graph[start])

        for start, end in queue:
            if not dfs(start, end):
                return False
            visited = set()
            
        return True
