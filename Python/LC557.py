class Solution:
    def reverseWords(self, s: str) -> str:
        s2 = s.split()
        for i in range(len(s2)):
            s2[i] = s2[i][::-1]
        return ' '.join(s2)