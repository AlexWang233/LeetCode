class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wl = len(words[0])
        d_orig = Counter(words)
        n = len(words)
        l = wl * n
        ans = []

        def checkSubstr(i):
            d = d_orig.copy()
            count = 0
            for j in range(i, i + l, wl):
                w = s[j : j + wl]
                if d[w] > 0:
                    d[w] -= 1
                    count += 1
                else:
                    break
            return count == n


        for i in range(len(s) - l + 1):
            if checkSubstr(i):
                ans.append(i)

        return ans