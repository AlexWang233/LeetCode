class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 = 1
        dp2 = 0 
        l = len(s)
        
        for i in range(l):
            dp = 0
            if s[i] != '0':
                dp += dp1
            if i > 0 and (s[i-1] == '1' or (s[i-1] == '2' and int(s[i]) < 7)):
                dp += dp2
            dp2 = dp1
            dp1 = dp
        
        return dp1
            