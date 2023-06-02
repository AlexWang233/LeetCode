
from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = defaultdict(lambda: 0)
        for c in ransomNote:
            i = magazine[d[c]:].find(c)
            if i == -1:
                return False
            d[c] = i+d[c]+1
        print(d)
        return True