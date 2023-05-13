class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        d = defaultdict(lambda: set())
        d2 = defaultdict(lambda: set())
        for i, j in connections:
            d[i].add(j)
            d2[j].add(i)

        q = set([0])
        ans = 0
        visited = set()
        while len(q) > 0:
            cur = set()
            for node in q:
                visited.add(node)
                for n2 in d[node]:
                    if n2 in visited:
                        continue
                    cur.add(n2)
                    ans += 1
                for n2 in d2[node]:
                    if n2 in visited:
                        continue
                    cur.add(n2)
            q = cur
        return ans
