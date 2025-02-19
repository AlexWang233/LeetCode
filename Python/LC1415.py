class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['c', 'b', 'a']
        q = deque([''])
        res = ""
        while k > 0 and len(q) > 0:
            cur = q.pop()
            if len(cur) == n:
                k -= 1
                res = cur
                continue
            for c in letters:
                if len(cur) > 0 and cur[-1] == c:
                    continue
                q.append(cur + c)
        return "" if k > 0 else res