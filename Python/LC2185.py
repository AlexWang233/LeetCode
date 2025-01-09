class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        l = len(pref)
        ans = 0
        for w in words:
            if len(w) < l:
                continue
            if w[:l] == pref:
                ans += 1
        return ans