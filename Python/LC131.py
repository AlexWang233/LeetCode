class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(s: str):
            return s == s[::-1]

        def dfs(s):
            if not s:
                res.append(arr.copy())
                return
            for i in range(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    arr.append(s[:i])
                    dfs(s[i:])
                    arr.pop()
        res = []
        arr = []
        dfs(s)
        return res