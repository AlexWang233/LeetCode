class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [0] + [len(s) + 1] * len(s)

        def dfs(text):

            l = len(text)
            cur_min = l

            if dp[l] <= len(s):
                return dp[l]
                
            for word in dictionary:
                l2 = len(word)
                if text[:l2] == word:
                    res = dfs(text[l2:])
                    cur_min = min(cur_min, res)

            cur_min = min(cur_min, 1 + dfs(text[1:]))
            dp[l] = cur_min
            return cur_min

        res = dfs(s)
        return res

            