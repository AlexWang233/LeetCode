class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for w in s:
            if w == '*':
                ans.pop()
            else:
                ans.append(w)

        return ''.join(ans)