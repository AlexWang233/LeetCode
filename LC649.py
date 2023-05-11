class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = deque([])
        dq = deque([])
        count = 0
        for s in senate:
            if s == 'R':
                rq.append(count)
            else:
                dq.append(count)
            count += 1
        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()
            if r > d:
                dq.append(count)
            else:
                rq.append(count)
            count += 1

        if len(rq) > len(dq):
            return "Radiant"
        return "Dire"