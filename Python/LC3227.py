class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        cnt = 0
        for c in s:
            if c in vowels:
                return True
        return False