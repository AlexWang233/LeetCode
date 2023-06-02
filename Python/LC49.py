from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(lambda: [])
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return list(d.values())