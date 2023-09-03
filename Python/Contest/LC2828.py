class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        l = len(s)
        if len(words) != l:
            return False
        for i in range(l):
            if words[i][0] != s[i]:
                return False
        return True
