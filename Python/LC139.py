from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([s])
        seen = set()
        
        while q:
            s = q.popleft()
            for w in wordDict:
                if s.startswith(w):
                    ns = s[len(w):]
                    if ns == '':
                        return True
                    if ns not in seen:
                        seen.add(ns)
                        q.append(ns)
                        
        return False