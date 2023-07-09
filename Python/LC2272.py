class Solution:
    def largestVariance(self, s: str) -> int:
        c1 = c2 = 0
        res = 0

        # initialize all pairs of unique characters in s
        pairs = [(a, b) for a in set(s) for b in set(s) if a != b]

        for _ in range(2):
            for a, b in pairs:
                c1 = c2 = 0
                for c in s:
                    if c == a:
                        c1 += 1
                    elif c == b:
                        c2 += 1
                    else:
                        continue

                    if c1 < c2:
                        # reset count in this case since order of pairs do matter
                        c1 = c2 = 0
                    elif c1 > 0 and c2 > 0:
                        # only update res when both characters already exist in substring
                        res = max(res, c1 - c2)
            
            # reverse string so we start the other way around
            s = s[::-1]

        return res
                    
                
