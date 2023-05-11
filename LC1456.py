class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        cur = 0
        for i in range(k):
            if s[i] in vowels:
                cur += 1
        ans = cur
        for i in range(k, len(s)):
            if s[i] in vowels:
                cur += 1
            if s[i-k] in vowels:
                cur -= 1
            ans = max(ans, cur)

        return ans