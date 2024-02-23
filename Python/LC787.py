class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(lambda: [])
        for f in flights:
            graph[f[0]].append((f[1], f[2]))
        arr = {src: 0}
        count = 0
        while count <= k:
            cur = arr.copy()
            for start in arr:
                for end, p in graph[start]:
                    if end not in cur:
                        cur[end] = arr[start] + p
                    else:
                        cur[end] = min(cur[end], arr[start] + p)
            count += 1
            arr = cur.copy()
        return arr[dst] if dst in arr else -1
            

