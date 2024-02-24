class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        res = {0, firstPerson}
        meetings.sort(key = lambda x: x[-1])
        for _, group in groupby(meetings, key = lambda x: x[-1]):
            q = set()
            graph = defaultdict(list)
            for a, b, _ in group:
                graph[a].append(b)
                graph[b].append(a)
                if a in res:
                    q.add(a)
                if b in res:
                    q.add(b)
            q = deque(q)
            while q:
                x = q.popleft()
                for y in graph[x]:
                    if y not in res:
                        res.add(y)
                        q.append(y)
        return res