class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        zeroes = s.count('0')
        ones = 0
        val = 0
        exp = 1

        for n in range(len(s) - 1, -1, -1):
            if s[n] == '1':
                if val + exp > k:
                    continue
                val += exp
                ones += 1
            exp <<= 1
            if exp > k:
                break
                
        return zeroes + ones