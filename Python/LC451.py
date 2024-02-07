class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        c = sorted(c.items(), key = lambda item: (item[1], item[0]), reverse = True)

        ans = ''
        for i in range(len(c)):
            ans += c[i][0] * c[i][1]
        return ans