class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for start, end in sorted(tickets)[::-1]:
            d[start].append(end)
        res = []

        def dfs(stop):
            while d[stop]:
                dfs(d[stop].pop())
            res.append(stop)
        
        dfs('JFK')
        return res[::-1]