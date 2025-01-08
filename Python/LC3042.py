class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixAndSuffix(s1, s2):
            n1, n2 = len(s1), len(s2)
            if n1 > n2:
                return False
            return s2[:n1] == s1 and s2[-n1:] == s1
        
        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        return ans