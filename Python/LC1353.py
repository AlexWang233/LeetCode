class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        hp = []
        i = 0
        l = len(events)
        ans = 0
        last_day = max(end for _, end in events)

        for day in range(1, last_day + 1):
            while i < l and events[i][0] == day:
                heapq.heappush(hp, events[i][1])
                i += 1
            while hp and hp[0] < day:
                heapq.heappop(hp)
            if hp:
                heapq.heappop(hp)
                ans += 1

        return ans
