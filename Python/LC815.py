class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        busDict = defaultdict(lambda: set())
        stopDict = defaultdict(lambda: set())
        
        i = 0
        for bus in routes:
            busDict[i] = set(bus)
            for stop in bus:
                stopDict[stop].add(i)
            i += 1

        q = set([source])
        visited = set()
        busVisited = set()
        ans = 0
        while q:
            cur = set()
            for stop in q:
                if stop == target:
                    return ans
                if stop not in visited:
                    visited.add(stop)
                    for bus in stopDict[stop]:
                        if bus in busVisited:
                            continue
                        busVisited.add(bus)
                        for stop in busDict[bus]:
                            cur.add(stop)
            ans += 1
            q = cur
        return -1
            