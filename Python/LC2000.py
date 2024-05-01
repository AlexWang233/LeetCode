class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        end = word.find(ch)
        return word[:end + 1][::-1] + word[end + 1:]
        