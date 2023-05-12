class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        for i in range(len(s)):
            if not s[i].isalpha() and not s[i].isdigit():
                continue
            while not s[r].isalpha() and not s[r].isdigit() and r > 0:
                r -= 1
            if i >= r:
                break
            if s[i].lower() != s[r].lower():
                return False
            r -= 1
        return True