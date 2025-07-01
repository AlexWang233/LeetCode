class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = ' '
        l = len(word)
        ans = 1
        i = 0
        while i < l:
            while i < l and word[i] == prev:
                i += 1
                ans += 1
            if i < l:
                prev = word[i]
            i += 1
        return ans