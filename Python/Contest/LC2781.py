class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        s = set(forbidden)
        res = 0
        r = len(word) - 1
        for l in range(len(word)-1, -1, -1):
            # since all words in forbidden have length <= 10, only check next 10 characters
            for i in range(l, min(l + 10, r + 1)):
                # if word from l to i is invalid, move right end to i - 1
                if word[l:i+1] in s:
                    r = i - 1
                    break
            res = max(res, r - l + 1)
        return res 