class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i = 0
        l = min(len(word1), len(word2))
        for i in range(l):
            ans.append(word1[i])
            ans.append(word2[i])

        if len(word1) > l:
            ans += word1[l:].split()

        if len(word2) > l:
            ans += word2[l:].split()

        return ''.join(ans)