class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def mask_vowels(s: str) -> str:
            return ''.join('a' if c in "aeiou" else c for c in s)

        wordset = set(wordlist)
        lower_map = defaultdict(lambda: "")
        masked_map = defaultdict(lambda: "")

        for w in wordlist:
            wl = w.lower()
            if len(lower_map[wl]) == 0:
                lower_map[wl] = w
            wm = mask_vowels(wl)
            if len(masked_map[wm]) == 0:
                masked_map[wm] = w

        ans = []

        for q in queries:
            if q in wordset:
                ans.append(q)
                continue
            ql = q.lower()
            if ql in lower_map.keys():
                ans.append(lower_map[ql])
                continue
            qm = mask_vowels(ql)
            ans.append(masked_map[qm])

        return ans
