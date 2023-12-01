class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1, s2 = "", ""
        for w in word1:
            s1 += w
        for w in word2:
            s2 += w
        return s1 == s2