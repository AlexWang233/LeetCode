class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        res = 0
        for w in words:
            c2 = Counter(w)
            t = True
            for key in c2.keys():
                if c2[key] > counter[key]:
                    t = False
                    break
            if t:
                res += len(w)

        return res