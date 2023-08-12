class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key = lambda x: -x[0])
        res = cur = 0
        arr = []
        seen = set()
        for i, (val, group) in enumerate(items):
            if i < k:
                if group in seen:
                    # add val to arr only if group is duplicate
                    arr.append(val)
                cur += val
            elif group not in seen:
                if not arr:
                    # we have found the optimal subsequence
                    # if the existing set contains no duplicate groups
                    break
                cur += val
                cur -= arr.pop()
            seen.add(group)
            res = max(res, cur + len(seen) ** 2)
        return res