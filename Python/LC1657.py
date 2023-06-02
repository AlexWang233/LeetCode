class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # First check if they use the same set of characters
        if set(word1) != set(word2):
            return False
        # Then check if they have same character frequency (not necessarily w.r.t. the same characters)
        return Counter(Counter(word1).values()) == Counter(Counter(word2).values())