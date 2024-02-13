class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def checkPalindrome(word):
            for i in range(len(word) // 2):
                if word[i] != word[~i]:
                    return False
            return True
        
        for w in words:
            if checkPalindrome(w):
                return w
        return ""