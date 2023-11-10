class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        l = len(adjacentPairs)
        mp = defaultdict(list)
        for a, b in adjacentPairs:
            mp[a].append(b)
            mp[b].append(a)

        start = -1
        for n, ngbr in mp.items():
            if len(ngbr) == 1:
                start = n
                break

        res = [start]
        prev = start
        seen = set([start])
        while len(res) <= l:
            for n in mp[prev]:
                if n not in seen:
                    seen.add(n)
                    res.append(n)
                    prev = n

        return res

